from enum import Enum
from pydantic import BaseModel


class MessageType(str, Enum):
    TEXT = 'text'
    HTML = 'html'


class ResendEmailModel(BaseModel):
    to: list[str]
    subject: str
    message_type: str
    message: str


class ResendEmailResult(BaseModel):
    id: str