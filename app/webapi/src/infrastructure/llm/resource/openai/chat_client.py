from .client import (
    AsyncOpenAIClient,
)
from .chat_model import (
    OpenAIChatModel,
    OpenAIChatResult,
)
from .chat_exception import (
    OpenAIChatError
)


class AsyncOpenAIChatClient(AsyncOpenAIClient):

    def __init__(self, api_key: str | None = None) -> None:
        super().__init__(api_key)

    async def chat(self, params: OpenAIChatModel) -> OpenAIChatResult:
        try:
            res = await self.client.chat.completions.create(
                model=params.model,
                messages=params.messages,
            )
            
            return OpenAIChatResult(
                model=res.model,
                content=res.choices[0].message.content,
                usage=res.usage.total_tokens
            )
        
        except Exception as e:
            raise OpenAIChatError(f"Invalid response from OpenAI API: {e}")
    
    