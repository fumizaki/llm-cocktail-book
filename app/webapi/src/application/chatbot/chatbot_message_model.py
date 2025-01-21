from ..model import Model


class CreateChatbotMessageModel(Model):
    chatbot_id: str
    meta: dict[str, str]
    prompt: str
