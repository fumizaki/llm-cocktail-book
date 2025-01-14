from typing import Type, Optional
from ..client import (
    AsyncAnthropicCoreClient,
)
from .model import (
    AnthropicChatModel,
    AnthropicChatResult,
)

class AsyncAnthropicChatClient(AsyncAnthropicCoreClient):

    def __init__(self, api_key: str | None = None) -> None:
        super().__init__(api_key)

    async def chat(self, params: AnthropicChatModel) -> AnthropicChatResult:
        res = await self.client.messages.create(
            max_tokens=1024,
            model=params.model,
            messages=params.messages,
        )
        return AnthropicChatResult(
            model=res.model,
            content=res.content[0].text,
            usage=res.usage.input_tokens + res.usage.output_tokens
        )
    
