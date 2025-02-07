from ..entity import Entity

class ChatbotVectorPoint(Entity):
    account_id: str
    chunks: list[str] | list[list[str]]
    vectors: list[float] | list[list[float]]