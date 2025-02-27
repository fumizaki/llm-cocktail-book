from fastapi import APIRouter, UploadFile, Form, File, status, HTTPException, Depends
from src.presentation.dependency.usecase.chatbot import implement_chatbot_usecase, implement_chatbot_message_usecase, implement_chatbot_index_usecase
from src.application.chatbot import ChatbotUsecase, ChatbotMessageUsecase, ChatbotIndexUsecase
from src.domain.chatbot import CreateChatbotModel, CreateChatbotMessageModel, CreateChatbotIndexModel

router = APIRouter()


@router.get("/chatbot")
async def get_all_chatbot(usecase: ChatbotUsecase = Depends(implement_chatbot_usecase)):
    result = await usecase.get_all_exec()
    return result

@router.post("/chatbot")
async def create_chatbot(form: CreateChatbotModel, usecase: ChatbotUsecase = Depends(implement_chatbot_usecase)):
    result = await usecase.create_exec(form)
    return result

@router.patch("/chatbot")
async def update_chatbot():
    pass

@router.delete("/chatbot")
async def delete_chatbot():
    pass

@router.get("/chatbot/message/{chatbot_id}")
async def get_chatbot_message(chatbot_id: str, usecase: ChatbotMessageUsecase = Depends(implement_chatbot_message_usecase)):
    result = await usecase.get_all_exec(chatbot_id)
    return result

@router.post("/chatbot/message")
async def create_chatbot_message(
    chatbot_id: str = Form(...),
    resource: str = Form(...),
    mode: str = Form(...),
    prompt: str = Form(...),
    images: list[UploadFile] = File(default=[]),
    docs: list[UploadFile] = File(default=[]),
    usecase: ChatbotMessageUsecase = Depends(implement_chatbot_message_usecase)
    ):
    form = CreateChatbotMessageModel(
        chatbot_id=chatbot_id,
        resource=resource,
        mode=mode,
        prompt=prompt
    )
    bytes_images = [img.file.read() for img in images]
    files = bytes_images
    result = await usecase.create_exec(form, files)
    return result

@router.get("/chatbot/index/{chatbot_id}")
async def get_all_chatbot_index(chatbot_id: str, usecase: ChatbotIndexUsecase = Depends(implement_chatbot_index_usecase)):
    result = await usecase.get_all_exec(chatbot_id)
    return result

@router.post("/chatbot/index")
async def create_chatbot_index(form: CreateChatbotIndexModel, usecase: ChatbotIndexUsecase = Depends(implement_chatbot_index_usecase)):
    result = await usecase.create_exec(form)
    return result

@router.patch("/chatbot/index")
async def update_chatbot_index():
    pass

@router.delete("/chatbot/index")
async def delete_chatbot_index():
    pass