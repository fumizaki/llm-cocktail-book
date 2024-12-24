from fastapi import Depends
from sqlalchemy.orm import Session
from src.application.chatbot.message.query import ChatbotMessageQuery
from src.infrastructure.postgresql.query.chatbot import ChatbotMessageQueryImpl
from src.infrastructure.postgresql.session import get_rdb_session


def implement_chatbot_message_query(session: Session = Depends(get_rdb_session)) -> ChatbotMessageQuery:
    return ChatbotMessageQueryImpl(session)

