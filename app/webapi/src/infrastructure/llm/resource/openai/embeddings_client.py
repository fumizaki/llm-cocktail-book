from .client import AsyncOpenAIClient
from .embeddings_model import (
    OpenAIEmbeddingsModel,
    OpenAIEmbeddingsResult,
)


class AsyncOpenAIEmbeddingsClient(AsyncOpenAIClient):

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
            vector=[d.embedding for d in res.data]
        )