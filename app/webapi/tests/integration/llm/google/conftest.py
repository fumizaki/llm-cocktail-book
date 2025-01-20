import os
from dotenv import load_dotenv
import pytest
from src.infrastructure.llm.resource.google import (
    AsyncGoogleAIChatClient,
)


# Load environment variables from .env file
load_dotenv()

@pytest.fixture
def api_key():
    """Get API key from environment variables"""
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        pytest.skip("GOOGLE_API_KEY not found in environment variables")
    return api_key



@pytest.fixture
def async_chat_client(api_key) -> AsyncGoogleAIChatClient:
    """Create and return an AsyncGoogleAIChatClient instance"""
    return AsyncGoogleAIChatClient(api_key=api_key)
