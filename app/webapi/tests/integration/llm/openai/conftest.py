import os
from dotenv import load_dotenv
import pytest
from src.infrastructure.llm.resource.openai import (
    AsyncOpenAIChatClient,
)


# Load environment variables from .env file
load_dotenv()

@pytest.fixture
def api_key():
    """Get API key from environment variables"""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        pytest.skip("OPENAI_API_KEY not found in environment variables")
    return api_key



@pytest.fixture
def async_chat_client(api_key) -> AsyncOpenAIChatClient:
    """Create and return an AsyncOpenAIChatClient instance"""
    return AsyncOpenAIChatClient(api_key=api_key)
