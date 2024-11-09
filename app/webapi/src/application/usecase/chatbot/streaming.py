from fastapi import HTTPException, status
from src.domain.entity.credential import Credential
from src.domain.schema.chatbot import Txt2TxtRequestParams
# from src.infrastructure.core.rdb.transaction import TransactionClient
from src.infrastructure.openai.chat import AsyncOpenAIChatClient


class ChatbotStreamingUsecase:
    def __init__(
        self,
        credential: Credential
    ) -> None:
        self.credential = credential


    async def txt2txt_exec(self, params: Txt2TxtRequestParams):
        print(f"{self.credential.id}: {params.prompt}")
        openai_chat_client = AsyncOpenAIChatClient()
        system_prompt = { "role": "system", "content": "You are a helpful assistant." }
        msg = openai_chat_client.chat_stream(messages=[system_prompt, {"role": "user", "content": params.prompt}])
        return msg