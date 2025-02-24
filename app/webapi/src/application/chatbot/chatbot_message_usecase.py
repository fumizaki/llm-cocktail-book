from datetime import datetime
from fastapi import HTTPException, status
from .chatbot_query import ChatbotQuery
from src.domain.account import AccountCredentialModel
from src.domain.chatbot import (
    AggChatbot,
    ChatbotMessage,
    CreateChatbotMessageModel,
    ChatbotMessageRepository,
    ChatbotVectorRepository
)
from src.domain.llm import LLMUsage, LLMUsageRepository
from src.infrastructure.database.rdb import TransactionClient
from src.infrastructure.llm import (
    TextGenerationClient,
    TextGenerationMessage,
    TextGenerationMessageRole,
    TextGenerationResponse,
    # Txt2TxtClient,
    # Txt2TxtResult,
    # Txt2TxtMessageRole,
    # Txt2TxtMessage,
    # Txt2VecClient,
    # Txt2VecResult
)
from src.infrastructure.logging import JsonLineLoggingClient

class ChatbotMessageUsecase:
    def __init__(
        self,
        credential: AccountCredentialModel,
        tx: TransactionClient,
        chatbot_query: ChatbotQuery,
        chatbot_message_repository: ChatbotMessageRepository,
        chatbot_vector_repository: ChatbotVectorRepository,
        llm_usage_repository: LLMUsageRepository
    ) -> None:
        self.credential = credential
        self.tx = tx
        self.chatbot_query = chatbot_query
        self.chatbot_message_repository = chatbot_message_repository
        self.chatbot_vector_repository = chatbot_vector_repository
        self.llm_usage_repository = llm_usage_repository
        self.logger = JsonLineLoggingClient.get_logger(self.__class__.__name__)


    async def get_all_exec(self, chatbot_id: str) -> AggChatbot:
        self.logger.info(f"Get All Chatbot Message execution started for account: {self.credential.account_id}")
        try:
            agg_chat_in_db: AggChatbot = self.chatbot_query.get_agg_chatbot(chatbot_id, self.credential.account_id)
            return agg_chat_in_db
        
        except HTTPException as http_exc:
            self.logger.error(f"HTTPException occurred: {http_exc.detail}")
            raise

        except Exception as exc:
            self.logger.critical(f"Unexpected error during token execution: {str(exc)}", exc_info=True)
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail='Internal Server Error'
            )



    async def create_exec(self, params: CreateChatbotMessageModel) -> ChatbotMessage:
        self.logger.info(f"Create Chatbot Message execution started for account: {self.credential.account_id}")

        try:
            self.logger.info(f"Get messages as context in Chatbot: {params.chatbot_id}")
            # コンテキストとして履歴を取得
            context_in_db: list[ChatbotMessage] = self.chatbot_message_repository.get_latest_list_exclude_deleted(params.chatbot_id, 6)

            prompt = params.prompt
            self.logger.info(f"Create Message with prompt")
            # DBへ保存
            self.chatbot_message_repository.create(ChatbotMessage(
                    chatbot_id=params.chatbot_id,
                    role=TextGenerationMessageRole.USER,
                    content=prompt,
                    created_at=datetime.now()
                ))
            

            # if self.chatbot_vector_repository.is_exists(params.chatbot_id):
            #     txt2vec = Txt2VecClient(resource='openai')
            #     txt2vec_result: Txt2VecResult = await txt2vec.generate(prompt)

            #     self.llm_usage_repository.create(
            #         LLMUsage(
            #             account_id=self.credential.account_id,
            #             resource=txt2vec_result.resource,
            #             model=txt2vec_result.model,
            #             task='txt2vec',
            #             usage=txt2vec_result.usage
            #         )
            #     )
                
            #     vector_points = self.chatbot_vector_repository.search(
            #         chatbot_id=params.chatbot_id,
            #         vector=txt2vec_result.vector,
            #         top_k=3
            #     )
            #     reference = "\n".join(["\n".join([chunk for chunk in point.chunks]) for point in vector_points])

            #     prompt = f"""\
            #     {prompt}
            #     事前知識だけではなく、提供された以下のコンテキストも使用してクエリに回答してください。\
            #     {reference}
            #     """
                
            self.logger.info(f"Create Message with LLM")
            gen_text = TextGenerationClient(
                resource=params.resource,
                mode=params.mode,
                context=[TextGenerationMessage(content=message.content, role=message.role) for message in context_in_db]
                )
            res: TextGenerationResponse = await gen_text.generate(content=prompt)

            # self.logger.info(f"Create Usage")
            # self.llm_usage_repository.create(
            #     LLMUsage(
            #         account_id=self.credential.account_id,
            #         resource=res.resource,
            #         model=res.model,
            #         task='txt2txt',
            #         usage=res.usage
            #     ))
            
            assistant_chatbot_message_in_db: ChatbotMessage = self.chatbot_message_repository.create(
                ChatbotMessage(
                    chatbot_id=params.chatbot_id,
                    role=TextGenerationMessageRole.ASSISTANT,
                    content=res.content,
                    created_at=datetime.now()
                ))
            
            self.tx.commit()
            
            return assistant_chatbot_message_in_db
            
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
