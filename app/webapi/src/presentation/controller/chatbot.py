from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from src.presentation.dependency.usecase.chatbot import implement_streaming_usecase
from src.application.usecase.chatbot.streaming import ChatbotStreamingUsecase
from src.domain.schema.chatbot import Txt2TxtRequestParams
from src.infrastructure.openai.chat import AsyncOpenAIChatClient


router = APIRouter()

@router.post("/chat")
async def txt2txt_openai(prompt: str):
    openai_chat_client = AsyncOpenAIChatClient()
    system_prompt = { "role": "system", "content": "You are a helpful assistant." }
    msg = await openai_chat_client.chat(messages=[system_prompt, {"role": "user", "content": prompt}])
    return msg

@router.post("/chat/stream")
async def txt2txt_openai_stream(form: Txt2TxtRequestParams, usecase: ChatbotStreamingUsecase = Depends(implement_streaming_usecase)):
    result = await usecase.txt2txt_exec(form)
    return StreamingResponse(result, media_type="text/event-stream")

