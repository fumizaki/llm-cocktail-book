from enum import Enum
from pydantic import BaseModel


class MessageType(str, Enum):
    TEXT = 'text'
    HTML = 'html'

class EmailContent(BaseModel):
    subject: str
    message_type: str
    message: str