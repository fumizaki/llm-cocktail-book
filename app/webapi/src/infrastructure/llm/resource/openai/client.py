import os
from dotenv import load_dotenv
from openai import AsyncOpenAI, OpenAI

load_dotenv()

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', '')


class OpenAIClient:

    def __init__(self, api_key: str = OPENAI_API_KEY) -> None:
        self.client = OpenAI(api_key=api_key)


class AsyncOpenAIClient:

    def __init__(self, api_key: str = OPENAI_API_KEY) -> None:
        self.client = AsyncOpenAI(api_key=api_key)