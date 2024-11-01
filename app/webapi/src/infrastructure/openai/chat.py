import os
from dotenv import load_dotenv
from enum import Enum
from openai import AsyncOpenAI


load_dotenv()

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', '')
OPENAI_TEMPERATURE = 0.5
OPENAI_TOP_P = 1.0


class OpenAIChatModel(str, Enum):
    GPT_4O_MINI = 'gpt-4o-mini'


class AsyncOpenAIChatClient:

    def __init__(self, api_key: str = OPENAI_API_KEY) -> None:
        self.client = AsyncOpenAI(api_key=api_key)
        
        
    async def chat(self, messages: list[dict[str, str]]):
        response = await self.client.chat.completions.create(
            model=OpenAIChatModel.GPT_4O_MINI,
            messages=messages,
            temperature=OPENAI_TEMPERATURE,
        )
        return response.choices[0].message.content


    async def chat_stream(self, messages: list[dict[str, str]]):
        response = await self.client.chat.completions.create(
            model=OpenAIChatModel.GPT_4O_MINI,
            messages=messages,
            temperature=OPENAI_TEMPERATURE,
            stream=True,
        )
        async for chunk in response:
            chunk_content = chunk.choices[0].delta.content
            if chunk_content is not None:
                yield chunk_content
                
                
            
        
        
        