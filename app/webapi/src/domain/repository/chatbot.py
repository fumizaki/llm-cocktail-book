from abc import ABC, abstractmethod
from src.domain.entity.chatbot import Chatbot


class ChatbotRepository(ABC):

    @abstractmethod
    def get_exclude_deleted(self, id: str) -> Chatbot:
        raise NotImplementedError
    
    @abstractmethod
    def get_all_exclude_deleted(self, account_id: str) -> list[Chatbot]:
        raise NotImplementedError

    @abstractmethod
    def create(self, entity: Chatbot) -> Chatbot:
        raise NotImplementedError
    
    @abstractmethod
    def update(self) -> Chatbot:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: str) -> Chatbot:
        raise NotImplementedError
    