from fastapi import Depends
from sqlalchemy.orm import Session
from src.application.chatbot import ChatbotQuery
from src.infrastructure.database.rdb.postgresql.query.chatbot import ChatbotQueryImpl
from src.infrastructure.database.rdb.postgresql.session import get_rdb_session


def implement_chatbot_query(session: Session = Depends(get_rdb_session)) -> ChatbotQuery:
    return ChatbotQueryImpl(session)

