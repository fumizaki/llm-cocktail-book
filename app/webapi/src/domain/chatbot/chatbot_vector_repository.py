from abc import ABC, abstractmethod
from .chatbot_vector_collection_entity import ChatbotVectorCollection
from .chatbot_vector_point_entity import ChatbotVectorPoint

class ChatbotVectorRepository(ABC):
    

    @abstractmethod
    def is_exists(self, chatbot_id: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    def create(self, entity: ChatbotVectorCollection) -> ChatbotVectorCollection:
        raise NotImplementedError
    
    @abstractmethod
    def update(self, chatbot_id: str, points: list[ChatbotVectorPoint]) -> bool:
        raise NotImplementedError

    @abstractmethod
    def delete(self, chatbot_id: str) -> bool:
        raise NotImplementedError
    