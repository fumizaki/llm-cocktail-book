from fastapi import Depends
from sqlalchemy.orm import Session
from src.application.chatbot import ChatbotQuery
from src.infrastructure.database.rdb import get_psql_session, ChatbotQueryImpl


def implement_chatbot_query(session: Session = Depends(get_psql_session)) -> ChatbotQuery:
    return ChatbotQueryImpl(session)

