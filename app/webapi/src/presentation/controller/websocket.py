from fastapi import APIRouter, Depends, WebSocket, WebSocketDisconnect
from src.presentation.dependency.authorization import get_credential_from_query
from src.infrastructure.core.websocket.connection import WebSocketConnectionClient


from src.application.usecase.chatbot.streaming import ChatbotStreamingUsecase
from src.domain.entity.credential import Credential
from src.domain.schema.chatbot import Txt2TxtRequestParams

router = APIRouter()

ws_connection_client = WebSocketConnectionClient()

@router.websocket("/chat")
async def ws_chat(ws: WebSocket, credential: Credential = Depends(get_credential_from_query)):
    usecase = ChatbotStreamingUsecase(credential)
    await ws_connection_client.connect(ws)    
    try:
        while True:
            data = await ws.receive_text()
            await ws_connection_client.send_text(ws, f"{credential.email}: {data}")
            msg = await usecase.txt2txt_exec(Txt2TxtRequestParams(prompt=data))
            await ws_connection_client.send_text(ws, msg)

    except WebSocketDisconnect:
        await ws_connection_client.disconnect(ws)
