from fastapi import HTTPException, status
from src.domain.account import AccountCredentialModel
from src.domain.chatbot import ChatbotIndex, CreateChatbotIndexModel, ChatbotIndexRepository, ChatbotVectorRepository, ChatbotVectorCollection, ChatbotVectorPoint
from src.domain.llm import LLMUsage, LLMUsageRepository
from src.infrastructure.database.rdb import TransactionClient
from src.infrastructure.llm import Txt2VecClient, Txt2VecResult
from src.infrastructure.logging import JsonLineLoggingClient


class ChatbotIndexUsecase:
    def __init__(
        self,
        credential: AccountCredentialModel,
        tx: TransactionClient,
        chatbot_index_repository: ChatbotIndexRepository,
        chatbot_vector_repository: ChatbotVectorRepository,
        llm_usage_repository: LLMUsageRepository
    ) -> None:
        self.credential = credential
        self.tx = tx
        self.chatbot_index_repository = chatbot_index_repository
        self.chatbot_vector_repository = chatbot_vector_repository
        self.llm_usage_repository = llm_usage_repository
        self.logger = JsonLineLoggingClient.get_logger(self.__class__.__name__)


    async def get_all_exec(self, chatbot_id: str) -> list[ChatbotIndex]:
        self.logger.info(f"Get All Chatbot Index execution started for account: {self.credential.account_id}")
        try:
            chatbot_index_in_db: list[ChatbotIndex] = self.chatbot_index_repository.get_all_exclude_deleted(chatbot_id)
            return chatbot_index_in_db
        
        except HTTPException as http_exc:
            self.logger.error(f"HTTPException occurred: {http_exc.detail}")
            raise

        except Exception as exc:
            self.logger.critical(f"Unexpected error during token execution: {str(exc)}", exc_info=True)
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail='Internal Server Error'
            )


    async def create_exec(self, params: CreateChatbotIndexModel) -> ChatbotIndex:
        self.logger.info(f"Create Chatbot Index execution started for account: {self.credential.account_id}")

        try:
            prompt = params.content

            self.logger.info(f"Create Vector with LLM")
            txt2vec = Txt2VecClient(params.resource)
            txt2vec_res : Txt2VecResult = await txt2vec.generate(prompt)

            self.logger.info(f"Create Usage")
            self.llm_usage_repository.create(
                LLMUsage(
                    account_id=self.credential.account_id,
                    resource=txt2vec_res.resource,
                    model=txt2vec_res.model,
                    task='txt2vec',
                    usage=txt2vec_res.usage
                ))

            self.logger.info(f"Create Index")
            chatbot_index_in_db: ChatbotIndex = self.chatbot_index_repository.create(
                ChatbotIndex(
                    chatbot_id=params.chatbot_id,
                    title=params.title,
                    content=params.content
                )
            )
            
            self.logger.info(f"Create Vector Collection")
            self.chatbot_vector_repository.create(
                ChatbotVectorCollection(
                    chatbot_id=params.chatbot_id,
                    size=len(txt2vec_res.vector),
                    points=[ChatbotVectorPoint(id=chatbot_index_in_db.id, chunks=txt2vec_res.chunks, vector=txt2vec_res.vector)]
                )
            )

            self.tx.commit()

            return chatbot_index_in_db

        except HTTPException as http_exc:
            self.logger.error(f"HTTPException occurred: {http_exc.detail}")
            self.tx.rollback()
            raise

        except Exception as exc:
            self.logger.critical(f"Unexpected error during token execution: {str(exc)}", exc_info=True)
            self.tx.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail='Internal Server Error'
            )
