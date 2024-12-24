from src.domain.entity.core import CoreEntity


class ChatbotMessage(CoreEntity):
    chatbot_id: str
    role: str
    content: str

