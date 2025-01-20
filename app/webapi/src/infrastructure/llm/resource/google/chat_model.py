from enum import Enum
from pydantic import BaseModel


class GoogleAIChatMessageRole(str, Enum):
    USER = 'user'
    MODEL = 'model'


class GoogleAIChatMessage(BaseModel):
    parts: str
    role: GoogleAIChatMessageRole


class GoogleAIChatModel(BaseModel):
    model: str
    contents: list[GoogleAIChatMessage]
    

class GoogleAIChatResult(BaseModel):
    model: str
    content: str
    usage: int