from fastapi import Depends
from sqlalchemy.orm import Session
from src.domain.repository.chatbot import ChatbotRepository
from src.infrastructure.database.rdb.postgresql.repository.chatbot import ChatbotRepositoryImpl
from src.infrastructure.database.rdb.postgresql.session import get_rdb_session


def implement_chatbot_repository(session: Session = Depends(get_rdb_session)) -> ChatbotRepository:
    return ChatbotRepositoryImpl(session)

