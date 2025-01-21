from ..entity import Entity

class ChatbotMessage(Entity):
    chatbot_id: str
    role: str
    content: str

