import uuid
from pydantic import Field
from pydantic import BaseModel

class Model(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))

class ChatbotIndexCollectionModel(Model):
    collection_name: str
    size: int


class ChatbotIndexPointModel(Model):
    collection_name: str
    chunks: list[str] | list[list[str]]
    vectors: list[float] | list[list[float]]