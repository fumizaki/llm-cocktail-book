import os
from dotenv import load_dotenv
from anthropic import Anthropic, AsyncAnthropic

load_dotenv()

ANTHROPIC_API_KEY = os.environ.get('ANTHROPIC_API_KEY', '')


class AnthropicCoreClient:

    def __init__(self, api_key: str = ANTHROPIC_API_KEY) -> None:
        self.client = Anthropic(api_key=api_key)


class AsyncAnthropicCoreClient:

    def __init__(self, api_key: str = ANTHROPIC_API_KEY) -> None:
        self.client = AsyncAnthropic(api_key=api_key)

