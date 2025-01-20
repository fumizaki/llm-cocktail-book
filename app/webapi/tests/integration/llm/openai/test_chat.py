import pytest
from pydantic import BaseModel
from src.infrastructure.llm.resource.openai import (
    AsyncOpenAIChatClient,
    OpenAIChatModel,
    OpenAIChatResult,
)


@pytest.mark.asyncio
async def test_simple_chat_completion(async_chat_client: AsyncOpenAIChatClient):
    """Test a simple chat completion request"""
    params = OpenAIChatModel(
        model="o1-mini",
        messages=[
            {"role": "user", "content": "What is 2+2?"}
        ]
    )
    
    result = await async_chat_client.chat(params)
    print(result)
    
    assert isinstance(result, OpenAIChatResult)
    assert result.model.startswith("o1-mini")
    assert result.content is not None
    assert result.usage > 0
    assert "4" in result.content.lower()


