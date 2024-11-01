import os
from dotenv import load_dotenv
import re
from typing import Optional
from enum import Enum
from pydantic import BaseModel
from openai import AsyncOpenAI


load_dotenv()

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', '')


class OpenAIVectorSearchDetail(BaseModel):
    similarity: float
    chunk: str


class OpenAIVectorizeResponse(BaseModel):
    model: str
    usage: int
    prompt: str
    vector: list[float]


class OpenAIVectorSearchResponse(BaseModel):
    model: str
    result: str
    usage: int


class OpenAIEmbeddingsModel(str, Enum):
    EMBEDDING3_SMALL = 'text-embedding-3-small'
    EMBEDDING3_LARGE = 'text-embedding-3-large'


class AsyncOpenAIEmbeddingsClient:

    def __init__(
        self,
        api_key: str = OPENAI_API_KEY,
    ) -> None:
        self.openai = AsyncOpenAI(api_key=api_key)

    @staticmethod
    def split_text(text: str, delimiters: list[str] | None = ['\n']) -> list[str]:
        """
        delimiters: list[str] | None = ['\n', ',', '.', '、', '。']
        """
        pattern = '|'.join(map(re.escape, delimiters))
        return [chunk.strip() for chunk in re.split(pattern, text) if chunk.strip()]

    async def vectorize(
        self,
        prompt: str,
        *,
        # dimensions: int, # デフォルトで1536?
        model: Optional[OpenAIEmbeddingsModel] = OpenAIEmbeddingsModel.EMBEDDING3_SMALL
    ) -> OpenAIVectorizeResponse:
        try:

            response = await self.openai.embeddings.create(
                    input=prompt,
                    model=model
                )
            
            return OpenAIVectorizeResponse(
                model=model,
                usage=response.usage.prompt_tokens,
                prompt=prompt,
                vector=response.data[0].embedding
            )
        except Exception as e:
            print(f"Error during embedding generation: {e}")