from enum import Enum
from pydantic import BaseModel


class MessageRole(str, Enum):
    ASSISTANT = 'assistant'
    SYSTEM = 'system'
    USER = 'user'

class Message(BaseModel):
    prompt: str
    role: MessageRole
