from enum import Enum
from pydantic import BaseModel


class MessageType(str, Enum):
    TEXT = 'text'
    HTML = 'html'


class EmailModel(BaseModel):
    to: list[str]
    subject: str
    message_type: str
    message: str


class EmailResult(BaseModel):
    id: str