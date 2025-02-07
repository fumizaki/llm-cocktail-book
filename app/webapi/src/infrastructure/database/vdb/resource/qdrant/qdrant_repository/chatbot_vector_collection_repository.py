from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct
from app.webapi.src.domain.chatbot.chatbot_vector_point_entity import ChatbotVectorPoint
from src.domain.chatbot import ChatbotVectorCollection, ChatbotVectorRepository



class ChatbotVectorRepositoryImpl(ChatbotVectorRepository):

    def __init__(self, qdrant: QdrantClient) -> None:
        self._client = qdrant


    def is_exists(self, account_id: str) -> bool:
        return self._client.collection_exists(account_id)
    

    def create_collection(self, entity: ChatbotVectorCollection) -> ChatbotVectorCollection:
        self._client.create_collection(
            collection_name=entity.account_id,
            vectors_config=VectorParams(
                size=entity.size,
                distance=Distance.COSINE
            )
        )
        return entity
    

    def delete_collection(self, account_id: str) -> bool:
        return self._client.delete_collection(account_id)
    

    def upload_points(self, entity: ChatbotVectorPoint) -> ChatbotVectorPoint:
        self._client.upload_points(
            collection_name=entity.account_id,
            points=[
                PointStruct(
                    id=idx,
                    vector=vector,
                    payload={"chunk": chunk}
                ) for idx, (vector, chunk) in enumerate(zip(entity.vector, entity.chunks))
            ]
        )
        return entity