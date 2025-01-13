from abc import ABC, abstractmethod
from src.domain.entity.chatbot_message import ChatbotMessage


class ChatbotMessageRepository(ABC):

    @abstractmethod
    def get_exclude_deleted(self, id: str) -> ChatbotMessage:
        raise NotImplementedError
    
    @abstractmethod
    def get_all_exclude_deleted(self, chat_id: str) -> list[ChatbotMessage]:
        raise NotImplementedError
    
    @abstractmethod
    def get_latest_list_exclude_deleted(self, chatbot_id: str, limit: int) -> list[ChatbotMessage]:
        raise NotImplementedError

    @abstractmethod
    def create(self, entity: ChatbotMessage) -> ChatbotMessage:
        raise NotImplementedError
    
    @abstractmethod
    def update(self) -> ChatbotMessage:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: str) -> ChatbotMessage:
        raise NotImplementedError
    
    
    
    
    