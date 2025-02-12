from ..model import Model
from .chatbot_vector_point_model import ChatbotVectorPoint

class ChatbotVectorCollection(Model):
    chatbot_id: str
    size: int
    points: list[ChatbotVectorPoint]