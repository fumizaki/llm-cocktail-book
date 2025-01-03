from fastapi import APIRouter, status, HTTPException, Depends
from src.presentation.dependency.usecase.chatbot import implement_chatbot_usecase, implement_chatbot_message_usecase
from src.application.chatbot import CreateChatbotModel, ChatbotUsecase, ChatbotMessageUsecase, CreateChatbotMessageModel


router = APIRouter()


@router.get("/chatbot")
async def get_all_chatbot(usecase: ChatbotUsecase = Depends(implement_chatbot_usecase)):
    result = await usecase.get_all_exec()
    return result

@router.post("/chatbot")
async def create_chatbot(form: CreateChatbotModel, usecase: ChatbotUsecase = Depends(implement_chatbot_usecase)):
    result = await usecase.create_exec(form)
    return result

@router.get("/chatbot/messages/{chatbot_id}")
async def get_chatbot_messages(chatbot_id: str, usecase: ChatbotMessageUsecase = Depends(implement_chatbot_message_usecase)):
    result = await usecase.get_all_exec(chatbot_id)
    return result

@router.post("/chatbot/messages/{chatbot_id}")
async def create_chatbot_messages(chatbot_id: str, form: CreateChatbotMessageModel, usecase: ChatbotMessageUsecase = Depends(implement_chatbot_message_usecase)):
    result = await usecase.create_exec(chatbot_id, form)
    return result