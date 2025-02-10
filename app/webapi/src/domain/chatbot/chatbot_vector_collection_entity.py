from ..entity import Entity
from .chatbot_vector_point_entity import ChatbotVectorPoint

class ChatbotVectorCollection(Entity):
    chatbot_id: str
    size: int
    points: list[ChatbotVectorPoint]