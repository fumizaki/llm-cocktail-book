from fastapi import Depends
from sqlalchemy.orm import Session
from src.domain.chatbot import ChatbotRepository, ChatbotMessageRepository
from src.infrastructure.database.rdb import get_psql_session, ChatbotRepositoryImpl, ChatbotMessageRepositoryImpl


def implement_chatbot_repository(session: Session = Depends(get_psql_session)) -> ChatbotRepository:
    return ChatbotRepositoryImpl(session)

def implement_chatbot_message_repository(session: Session = Depends(get_psql_session)) -> ChatbotMessageRepository:
    return ChatbotMessageRepositoryImpl(session)

