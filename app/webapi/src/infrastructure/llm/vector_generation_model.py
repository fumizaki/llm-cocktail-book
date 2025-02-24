from typing import Union, Any
from enum import Enum
from pydantic import BaseModel



class VectorGenerationResource(str, Enum):
    OPENAI = 'openai'
    # GOOGLE = 'google'

    @classmethod
    def names(cls) -> list[str]:
        return [i.name for i in cls]

    @classmethod
    def values(cls) -> list[str]:
        return [i.value for i in cls]


class VectorGenerationResponse(BaseModel):
    resource: VectorGenerationResource
    model: str
    content: str
    vector: list[float]

