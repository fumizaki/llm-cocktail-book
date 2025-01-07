from abc import ABC, abstractmethod
from src.domain.aggregate.chatbot import AggChatbot

class ChatbotMessageQuery(ABC):

    @abstractmethod
    def get_agg_chatbot(self, chatbot_id: str, account_id: str) -> AggChatbot:
        raise NotImplementedError
    
    @abstractmethod
    def get_agg_chatbot_limited(self, chatbot_id: str, account_id: str, limit: int) -> AggChatbot:
        raise NotImplementedError
    
