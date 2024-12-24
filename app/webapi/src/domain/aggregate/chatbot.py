from src.domain.entity.chatbot import Chatbot
from src.domain.entity.chatbot_message import ChatbotMessage

class AggChatbot(Chatbot):
    messages: list[ChatbotMessage]