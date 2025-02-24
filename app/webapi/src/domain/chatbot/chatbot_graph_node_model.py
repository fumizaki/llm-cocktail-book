import uuid
from pydantic import Field
from ..model import Model

class ChatbotGraphNode(Model):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    chatbot_id: str
