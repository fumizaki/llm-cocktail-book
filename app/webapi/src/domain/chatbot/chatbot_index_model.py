from ..model import Model

class CreateChatbotIndexModel(Model):
    chatbot_id: str
    meta: dict[str, str]
    title: str
    content: str