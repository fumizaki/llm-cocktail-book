from typing import Union, Any
from enum import Enum
from pydantic import BaseModel

TextGenerationMessage = Union[
    str,
    list[str],
    tuple[str, str],
    dict[str, Any]
]

class TextGenerationMessageRole(str, Enum):
    ASSISTANT = 'assistant'
    SYSTEM = 'system'
    USER = 'user'

    @classmethod
    def names(cls) -> list[str]:
        return [i.name for i in cls]

    @classmethod
    def values(cls) -> list[str]:
        return [i.value for i in cls]


class TextGenerationResource(str, Enum):
    OPENAI = 'openai'
    GOOGLE = 'google'
    ANTHROPIC = 'anthropic'

    @classmethod
    def names(cls) -> list[str]:
        return [i.name for i in cls]

    @classmethod
    def values(cls) -> list[str]:
        return [i.value for i in cls]


class TextGenerationMode(str, Enum):
    DISCUSSION = 'discussion'
    CODE = 'code'
    # TODO: PROMPT = 'prompt'
    # TODO: TRANSLATION = 'translation'
    # TODO: SUMMARY = 'summary'

    @classmethod
    def names(cls) -> list[str]:
        return [i.name for i in cls]

    @classmethod
    def values(cls) -> list[str]:
        return [i.value for i in cls]
    

class TextGenerationMessage(BaseModel):
    content: str
    role: TextGenerationMessageRole


class TextGenerationResponse(BaseModel):
    resource: TextGenerationResource
    model: str
    content: str

