import uuid
from pydantic import Field
from ..model import Model

class ChatbotVectorPoint(Model):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    chunks: list[str]
    vector: list[list[float]]