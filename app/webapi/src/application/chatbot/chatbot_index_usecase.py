from fastapi import HTTPException, status
from ..credential import Credential
from .chatbot_index_model import CreateChatbotIndexModel
from src.domain.chatbot import ChatbotVectorRepository, ChatbotVectorCollection, ChatbotVectorPoint
from src.domain.llm import LLMUsage, LLMUsageRepository
from src.infrastructure.database.rdb import TransactionClient
from src.infrastructure.llm import Txt2VecClient, Txt2VecModel, Txt2VecResult
from src.infrastructure.logging import JsonLineLoggingClient


class ChatbotIndexUsecase:
    def __init__(
        self,
        credential: Credential,
        tx: TransactionClient,
        chatbot_vector_repository: ChatbotVectorRepository,
        llm_usage_repository: LLMUsageRepository
    ) -> None:
        self.credential = credential
        self.tx = tx
        self.chatbot_vector_repository = chatbot_vector_repository
        self.llm_usage_repository = llm_usage_repository
        self.logger = JsonLineLoggingClient.get_logger(self.__class__.__name__)

    async def create_exec(self, params: CreateChatbotIndexModel) -> bool:
        self.logger.info(f"Create Chatbot Index execution started for account: {self.credential.account_id}")

        try:
            prompt = params.content

            self.logger.info(f"Create Vector with LLM")
            txt2vec = Txt2VecClient()
            res : Txt2VecResult = await txt2vec.generate(
                Txt2VecModel(
                    meta=params.meta,
                    prompt=prompt
                )
            )

            self.logger.info(f"Create Usage")
            self.llm_usage_repository.create(
                LLMUsage(
                    account_id=self.credential.account_id,
                    resource=res.resource,
                    model=res.model,
                    task='txt2vec',
                    usage=res.usage
                ))

            # TODO: ChatbotIndexEntityを作成
            
            self.logger.info(f"Create Vector Collection")
            self.chatbot_vector_repository.create(
                ChatbotVectorCollection(
                    chatbot_id=params.chatbot_id,
                    size=len(res.vector),
                    points=[ChatbotVectorPoint(chunks=res.chunks, vector=res.vector)]
                )
            )

            self.tx.commit()

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

# from src.application.core import Credential
# from src.infrastructure.llm.txt2vec import LLMTxt2VecClient, VectorGenerationMeta, Txt2VecModel, Txt2VecResult
# from src.infrastructure.database.vdb.qdrant.session import QdrantSessionClient

# class ChatbotIndexUsecase:
#     def __init__(
#         self,
#         credential: Credential
#     ) -> None:
#         self.credential = credential


#     async def create_exec(self, chatbot_id: str, prompt: str):
#         try:
#             txt2vec = LLMTxt2VecClient()
#             res = await txt2vec.generate(
#                 Txt2VecModel(
#                     meta=VectorGenerationMeta(
#                         llm='openai'
#                     ),
#                     prompt=prompt
#                 )
#             )
#             vdb = QdrantSessionClient()
#             vdb.create_collection(collection_name=chatbot_id, vector_size=1536)
#             vdb.upsert_points(collection_name=chatbot_id, vectors=res.content, chunks=res.chunks)
#             return True

#         except Exception as e:
#             print(e)

#         finally:
#             pass