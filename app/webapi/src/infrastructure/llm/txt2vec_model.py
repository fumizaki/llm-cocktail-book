from enum import Enum
from pydantic import BaseModel

class Txt2VecLLMMessage(BaseModel):
    prompt: str


class Txt2VecResource(str, Enum):
    OPENAI = 'openai'
    

class GenerationMeta(BaseModel):
    resource: Txt2VecResource


class VectorGenerationMeta(GenerationMeta):
    pass


class Txt2VecModel(BaseModel):
    meta: VectorGenerationMeta
    prompt: str


class Txt2VecResult(BaseModel):
    resource: Txt2VecResource
    model: str
    usage: int
    chunks: list[str]
    vector: list[float]