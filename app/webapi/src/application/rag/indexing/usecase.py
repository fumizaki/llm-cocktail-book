from src.application.core import Credential
# from src.infrastructure.openai.embeddings import AsyncOpenAIEmbeddingsClient
from src.infrastructure.database.vdb.qdrant.session import QdrantSessionClient


class RagIndexingUsecase:

    def __init__(self):
        self.params = {'collection_name': 'test'}

    async def prompt_indexing_exec(self, prompt: str):
        # print('テキストを分割します')
        # chunks = AsyncOpenAIEmbeddingsClient.split_text(prompt, delimiters=['\n'])
        # openai_embeddings_client = AsyncOpenAIEmbeddingsClient()
        # vectors = []
        # print('分割したテキストをベクトル化します')
        # for chunk in chunks:
        #     response = await openai_embeddings_client.vectorize(prompt=chunk)
        #     vectors.append(response.vector)
        
        # qdrant_client = QdrantSessionClient()
        # print(qdrant_client.is_alive())
        # qdrant_client.create_collection(collection_name=self.params['collection_name'], vector_size=len(vectors[0]))
        # print('pointをupsertします')
        # qdrant_client.upsert_points(collection_name=self.params['collection_name'], vectors=vectors, chunks=chunks)
        return True