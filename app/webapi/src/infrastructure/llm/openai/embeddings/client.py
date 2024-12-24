import re
from typing import Optional
from src.infrastructure.llm.openai.core import AsyncOpenAICoreClient
from .model import (
    OpenAIEmbeddingsModel,
    OpenAIEmbeddingsResult,
)


class AsyncOpenAIEmbeddingsClient(AsyncOpenAICoreClient):

    def __init__(self, api_key: str | None = None) -> None:
        super().__init__(api_key)

    async def vectorize(self, params: OpenAIEmbeddingsModel) -> OpenAIEmbeddingsResult:

        res = await self.client.embeddings.create(
                input=params.prompt,
                model=params.model
            )
        
        return OpenAIEmbeddingsResult(
            model=res.model,
            usage=res.usage.prompt_tokens,
            vector=res.data[0].embedding
        )