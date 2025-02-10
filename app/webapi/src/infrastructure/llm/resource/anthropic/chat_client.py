from .client import (
    AsyncAnthropicClient,
)
from .chat_model import (
    AnthropicChatModel,
    AnthropicChatResult,
)
from .chat_exception import (
    AnthropicChatError
)

class AsyncAnthropicChatClient(AsyncAnthropicClient):

    def __init__(self, api_key: str | None = None) -> None:
        super().__init__(api_key)

    async def chat(self, params: AnthropicChatModel) -> AnthropicChatResult:
        try:
            res = await self.client.messages.create(
                max_tokens=8192,
                model=params.model,
                messages=params.messages,
            )
            return AnthropicChatResult(
                model=res.model,
                content=res.content[0].text,
                usage=res.usage.input_tokens + res.usage.output_tokens
            )
        
        except Exception as e:
            raise AnthropicChatError(f"Invalid response from OpenAI API: {e}")
    
