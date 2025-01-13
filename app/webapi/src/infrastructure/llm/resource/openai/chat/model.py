from enum import Enum
from typing import TypeVar
from openai.types.chat_model import ChatModel as ChatModel
from openai import NotGiven as NotGiven, NOT_GIVEN as NOT_GIVEN
from pydantic import BaseModel


ResponseFormat = TypeVar("ResponseFormat", bound=BaseModel)


class OpenAIChatMessageRole(str, Enum):
    ASSISTANT = 'assistant'
    SYSTEM = 'system'
    USER = 'user'


class OpenAIChatMessage(BaseModel):
    content: str
    role: OpenAIChatMessageRole


class OpenAIChatModel(BaseModel):
    model: ChatModel
    messages: list[OpenAIChatMessage]
    

class OpenAIChatResult(BaseModel):
    model: ChatModel
    content: str
    usage: int