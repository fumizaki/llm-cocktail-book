from .chatbot_entity import Chatbot
from .chatbot_message_entity import ChatbotMessage

class AggChatbot(Chatbot):
    messages: list[ChatbotMessage]