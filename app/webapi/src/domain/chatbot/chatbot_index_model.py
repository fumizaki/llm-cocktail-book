from ..model import Model

class CreateChatbotIndexModel(Model):
    chatbot_id: str
    resource: str
    title: str
    content: str