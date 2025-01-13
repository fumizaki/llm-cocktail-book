from enum import Enum
from typing import TypeVar
from pydantic import BaseModel


ResponseFormat = TypeVar("ResponseFormat", bound=BaseModel)


class GoogleAIChatMessageRole(str, Enum):
    ASSISTANT = 'assistant'
    SYSTEM = 'system'
    USER = 'user'


class GoogleAIChatMessage(BaseModel):
    content: str
    role: GoogleAIChatMessageRole


class GoogleAIChatModel(BaseModel):
    model: str
    messages: list[GoogleAIChatMessage]
    

class GoogleAIChatResult(BaseModel):
    model: str
    content: str
    usage: int