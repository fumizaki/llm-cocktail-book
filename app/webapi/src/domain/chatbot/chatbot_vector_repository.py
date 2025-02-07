from abc import ABC, abstractmethod
from .chatbot_vector_collection_entity import ChatbotVectorCollection
from .chatbot_vector_point_entity import ChatbotVectorPoint

class ChatbotVectorRepository(ABC):
    

    @abstractmethod
    def is_exists(self, account_id: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    def create_collection(self, entity: ChatbotVectorCollection) -> ChatbotVectorCollection:
        raise NotImplementedError

    @abstractmethod
    def delete_collection(self, account_id: str) -> bool:
        raise NotImplementedError
    
    @abstractmethod
    def upload_points(self, entity: ChatbotVectorPoint) -> ChatbotVectorPoint:
        raise NotImplementedError