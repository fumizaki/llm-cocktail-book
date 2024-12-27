from fastapi import Depends
from sqlalchemy.orm import Session
from src.presentation.dependency.authorization import get_credential_from_header
from src.presentation.dependency.query.chatbot import implement_chatbot_message_query
from src.application.chatbot import ChatbotUsecase, ChatbotMessageUsecase, ChatbotMessageQuery
from src.application.core import Credential
from src.domain.repository.chatbot import ChatbotRepository
from src.infrastructure.database.rdb.postgresql.session import get_rdb_session
from src.infrastructure.database.rdb.transaction import TransactionClient


def implement_chatbot_usecase(
        credential: Credential = Depends(get_credential_from_header),
        session: Session = Depends(get_rdb_session),
        chatbot_repository: ChatbotRepository = Depends(implement_chatbot_message_query)
    ):
    return ChatbotUsecase(
        credential,
        TransactionClient(session),
        chatbot_repository
        )

def implement_chatbot_message_usecase(
       credential: Credential = Depends(get_credential_from_header),
       session: Session = Depends(get_rdb_session),
       chatbot_message_query: ChatbotMessageQuery = Depends(implement_chatbot_message_query)
    ):
    return ChatbotMessageUsecase(
        credential,
        TransactionClient(session),
        chatbot_message_query
        )