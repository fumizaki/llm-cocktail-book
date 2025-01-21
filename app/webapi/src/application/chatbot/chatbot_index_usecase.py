class ChatbotIndexUsecase:
    pass

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