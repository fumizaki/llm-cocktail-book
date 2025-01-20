from enum import Enum
from pydantic import BaseModel

class Txt2VecLLMMessage(BaseModel):
    prompt: str


class Txt2VecLLM(str, Enum):
    OPENAI = 'openai'
    

class GenerationMeta(BaseModel):
    llm: Txt2VecLLM


class VectorGenerationMeta(GenerationMeta):
    pass


class Txt2VecModel(BaseModel):
    meta: VectorGenerationMeta
    prompt: str


class Txt2VecResult(BaseModel):
    llm: Txt2VecLLM
    model: str
    usage: int
    chunks: list[str]
    content: list[float]