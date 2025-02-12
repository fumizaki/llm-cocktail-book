from pydantic import BaseModel
from openai.types.embedding_model import EmbeddingModel as EmbeddingModel

class OpenAIEmbeddingsModel(BaseModel):
    model: EmbeddingModel
    prompt: list[str]

class OpenAIEmbeddingsResult(BaseModel):
    model: EmbeddingModel
    usage: int
    vector: list[list[float]]