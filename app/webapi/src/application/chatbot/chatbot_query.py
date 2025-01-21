from abc import ABC, abstractmethod
from src.domain.chatbot import AggChatbot

class ChatbotQuery(ABC):

    @abstractmethod
    def get_agg_chatbot(self, chatbot_id: str, account_id: str) -> AggChatbot:
        raise NotImplementedError
    