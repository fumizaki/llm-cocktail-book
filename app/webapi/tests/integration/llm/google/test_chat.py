import pytest
from pydantic import BaseModel
from src.infrastructure.llm.resource.google import (
    AsyncGoogleAIChatClient,
    GoogleAIChatModel,
    GoogleAIChatResult,
)


@pytest.mark.asyncio
async def test_simple_chat_completion(async_chat_client: AsyncGoogleAIChatClient):
    """Test a simple chat completion request"""
    params = GoogleAIChatModel(
        model="gemini-pro",
        messages=[
            {"role": "user", "content": "What is 2+2?"}
        ]
    )
    
    result = await async_chat_client.chat(params)
    print(result)
    
    assert isinstance(result, GoogleAIChatResult)
    assert result.model.startswith("gemini-pro")
    assert result.content is not None
    assert result.usage > 0
    assert "4" in result.content.lower()


