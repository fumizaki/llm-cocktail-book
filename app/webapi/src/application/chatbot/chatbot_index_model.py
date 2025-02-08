from ..model import Model

class CreateChatbotIndexModel(Model):
    chatbot_id: str
    meta: dict[str, str]
    content: str