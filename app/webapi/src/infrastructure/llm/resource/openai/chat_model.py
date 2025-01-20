from enum import Enum
from typing import TypeVar, Type
from openai.types.chat_model import ChatModel as ChatModel
from pydantic import BaseModel


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

# TODO: o1-miniはresponse_formatに対応していないので、モデルによってパラメータを動的に変更する必要がある
# OpenAIChatResponseFormat = TypeVar("OpenAIChatResponseFormat", bound=BaseModel)
