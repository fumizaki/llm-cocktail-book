from enum import Enum
from typing import TypeVar
from pydantic import BaseModel
from anthropic.types import Model
from anthropic import NotGiven as NotGiven, NOT_GIVEN as NOT_GIVEN


class AnthropicChatMessageRole(str, Enum):
    ASSISTANT = 'assistant'
    SYSTEM = 'system'
    USER = 'user'


class AnthropicChatMessage(BaseModel):
    content: str
    role: AnthropicChatMessageRole


class AnthropicChatModel(BaseModel):
    model: Model
    messages: list[AnthropicChatMessage]
    

class AnthropicChatResult(BaseModel):
    model: Model
    content: str
    usage: int