from abc import ABC, abstractmethod
from .chatbot_index_entity import ChatbotIndex


class ChatbotIndexRepository(ABC):

    @abstractmethod
    def get_exclude_deleted(self, id: str) -> ChatbotIndex:
        raise NotImplementedError
    
    @abstractmethod
    def get_all_exclude_deleted(self, chatbot_id: str) -> list[ChatbotIndex]:
        raise NotImplementedError

    @abstractmethod
    def create(self, entity: ChatbotIndex) -> ChatbotIndex:
        raise NotImplementedError
    
    @abstractmethod
    def update(self) -> ChatbotIndex:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: str) -> ChatbotIndex:
        raise NotImplementedError
    
    
    
    
    