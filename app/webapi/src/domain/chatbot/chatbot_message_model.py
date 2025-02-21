from ..model import Model


class CreateChatbotMessageModel(Model):
    chatbot_id: str
    resource: str
    mode: str
    prompt: str
