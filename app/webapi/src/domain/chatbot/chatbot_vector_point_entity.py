from ..entity import Entity

class ChatbotVectorPoint(Entity):
    chunks: list[str]
    vector: list[float]