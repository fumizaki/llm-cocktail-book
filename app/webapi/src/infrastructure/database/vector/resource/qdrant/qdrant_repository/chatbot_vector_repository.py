from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct, ScoredPoint
from src.domain.chatbot import ChatbotVectorCollection, ChatbotVectorPoint, ChatbotVectorRepository



class ChatbotVectorRepositoryImpl(ChatbotVectorRepository):

    def __init__(self, qdrant: QdrantClient) -> None:
        self._client = qdrant


    def is_exists(self, chatbot_id: str) -> bool:
        return self._client.collection_exists(chatbot_id)
    

    def create(self, entity: ChatbotVectorCollection) -> ChatbotVectorCollection:

        if not self.is_exists(entity.chatbot_id):
            collection_result = self._client.create_collection(
                collection_name=entity.chatbot_id,
                vectors_config=VectorParams(
                    size=entity.size,
                    distance=Distance.COSINE
                )
            )
            if not collection_result:
                raise

        self._client.upload_points(
            collection_name=entity.chatbot_id,
            points=[
                PointStruct(
                    id=point.id,
                    vector=point.vector,
                    payload={ "chunk": point.chunks }
                ) for point in entity.points
            ]
        )
        return entity
    

    def update(self, chatbot_id: str, points: list[ChatbotVectorPoint]) -> bool:
        self._client.upsert(
            collection_name=chatbot_id,
            points=[
                PointStruct(
                    id=point.id,
                    vector=point.vector,
                    payload={ "chunk": point.chunks }
                ) for point in points
            ]
        )
        return True
    

    def delete(self, chatbot_id: str) -> bool:
        return self._client.delete_collection(chatbot_id)
    

    def search(self, chatbot_id: str, vector: list[float], top_k: int) -> list[ChatbotVectorPoint]:
        res: list[ScoredPoint] = self._client.search(
            collection_name=chatbot_id,
            query_vector=vector,
            limit=top_k
        )
        return [
            ChatbotVectorPoint(
                id=p.id,
                vector=vector,
                chunks=p.payload['chunk']
            ) for p in res
        ]
    
