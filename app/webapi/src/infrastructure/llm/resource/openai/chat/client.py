from typing import Type, Optional
from ..core import (
    AsyncOpenAICoreClient,
)
from .model import (
    OpenAIChatModel,
    OpenAIChatResult,
    ResponseFormat,
    NOT_GIVEN,
    NotGiven
)

class AsyncOpenAIChatClient(AsyncOpenAICoreClient):

    def __init__(self, api_key: str | None = None) -> None:
        super().__init__(api_key)

    async def chat(self, params: OpenAIChatModel, response_format: Optional[Type[ResponseFormat]] | NotGiven = NOT_GIVEN ) -> OpenAIChatResult:
        res = await self.client.chat.completions.create(
            model=params.model,
            messages=params.messages,
            response_format=response_format
        )
        return OpenAIChatResult(
            model=res.model,
            content=res.choices[0].message.content,
            usage=res.usage.total_tokens
        )
    
