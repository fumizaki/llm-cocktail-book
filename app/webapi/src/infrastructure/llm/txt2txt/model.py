from enum import Enum
from typing import TypeVar
from pydantic import BaseModel
from .code import ProgrammingLanguage


ResponseFormat = TypeVar("ResponseFormat", bound=BaseModel)

class Txt2TxtLLMMessageRole(str, Enum):
    ASSISTANT = 'assistant'
    SYSTEM = 'system'
    USER = 'user'


class Txt2TxtLLMMessage(BaseModel):
    prompt: str
    role: Txt2TxtLLMMessageRole


class Txt2TxtLLM(str, Enum):
    OPENAI = 'openai'
    # TODO: GOOGLE = 'google'
    # TODO: ANTHROPIC = 'anthropic'


class GenerationMode(str, Enum):
    TEXT = 'text'
    CODE = 'code'
    # TODO: PROMPT = 'prompt'
    # TODO: TRANSLATION = 'translation'
    

class GenerationMeta(BaseModel):
    llm: Txt2TxtLLM


class TextGenerationMeta(GenerationMeta):
    pass


class CodeGenerationMeta(GenerationMeta):
    lang: ProgrammingLanguage


class Txt2TxtModel(BaseModel):
    mode: GenerationMode
    meta: TextGenerationMeta | CodeGenerationMeta
    prompt: str
    context: list[Txt2TxtLLMMessage]


class Txt2TxtResult(BaseModel):
    llm: Txt2TxtLLM
    model: str
    usage: int
    content: str