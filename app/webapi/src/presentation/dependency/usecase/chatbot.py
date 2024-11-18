from fastapi import Depends
from src.application.usecase.chatbot.streaming import ChatbotStreamingUsecase
from src.domain.entity.credential import Credential
from src.presentation.dependency.authorization import get_credential_from_header


def implement_streaming_usecase(
        credential: Credential = Depends(get_credential_from_header),
    ):
    return ChatbotStreamingUsecase(
        credential
        )