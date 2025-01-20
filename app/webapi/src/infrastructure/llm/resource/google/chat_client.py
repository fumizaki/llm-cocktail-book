from .client import (
    GoogleAIClient,
)
from .chat_model import (
    GoogleAIChatModel,
    GoogleAIChatResult,
)
from .chat_exception import (
    GoogleAIChatError
)


class AsyncGoogleAIChatClient(GoogleAIClient):
    def __init__(self, api_key: str | None = None) -> None:
        super().__init__(api_key)

    async def chat(self, params: GoogleAIChatModel) -> GoogleAIChatResult:
        try:
            model = self.client.GenerativeModel(params.model)
            
            # contentsのparseで内部的エラーが発生している?
            # ref: https://github.com/google-gemini/generative-ai-python/issues/380
            res = await model.generate_content_async(contents=params.contents[0].parts)
            
            return GoogleAIChatResult(
                model=params.model,
                content=res.text,
                usage=res.usage_metadata.total_token_count
            )
        

        except Exception as e:
            raise GoogleAIChatError(f"Invalid response from GoogleAI API: {e}")
    


