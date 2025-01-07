from src.application.core.model import CoreModel


class CreateChatbotMessageModel(CoreModel):
    chatbot_id: str
    meta: dict[str, str]
    prompt: str
