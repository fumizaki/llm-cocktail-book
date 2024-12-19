from fastapi import HTTPException, status
from src.application.generation.code import Txt2CodeModel, PYTHON_PROMPT
from src.domain.entity.credential import Credential
from src.domain.type.llm import Message, MessageRole, ProgrammingLanguage
# from src.infrastructure.core.rdb.transaction import TransactionClient
from src.infrastructure.openai.chat import AsyncOpenAIChatClient


class CodeGenerationUsecase:
    def __init__(
        self,
        credential: Credential
    ) -> None:
        self.credential = credential

    def _build_system_prompt(language: ProgrammingLanguage, context: list[Message]) -> str:
        system_prompt = ''
        if language == ProgrammingLanguage.PYTHON:
            system_prompt += PYTHON_PROMPT

        context = context[::-1]
        for message in context:
            system_prompt += f"{message.role}: {message.prompt}"

        return system_prompt


    async def txt2code_exec(self, params: Txt2CodeModel):
        openai_chat_client = AsyncOpenAIChatClient()
        system_prompt = { "role": MessageRole.SYSTEM, "content": self._build_system_prompt(params.language, params.context) }
        msg = openai_chat_client.chat(messages=[system_prompt, {"role": MessageRole.USER, "content": params.prompt}])
        return msg