from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from src.infrastructure.openai.chat import AsyncOpenAIChatClient


router = APIRouter()

@router.post("/chat")
async def txt2txt_openai(prompt: str):
    openai_chat_client = AsyncOpenAIChatClient()
    system_prompt = { "role": "system", "content": "You are a helpful assistant." }
    msg = await openai_chat_client.chat(messages=[system_prompt, {"role": "user", "content": prompt}])
    return msg

@router.post("/chat/stream")
async def txt2txt_openai_stream(prompt: str):
    openai_chat_client = AsyncOpenAIChatClient()
    system_prompt = { "role": "system", "content": "You are a helpful assistant." }
    msg = openai_chat_client.chat_stream(messages=[system_prompt, {"role": "user", "content": prompt}])
    return StreamingResponse(msg, media_type="text/event-stream")

