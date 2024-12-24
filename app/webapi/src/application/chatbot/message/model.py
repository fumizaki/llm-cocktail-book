from src.application.core.model import CoreModel


class CreateChatbotMessageModel(CoreModel):
    mode: str
    meta: dict[str, str]
    prompt: str
    context: list[dict[str, str]]