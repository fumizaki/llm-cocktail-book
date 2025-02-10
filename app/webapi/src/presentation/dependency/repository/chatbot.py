from fastapi import Depends
from sqlalchemy.orm import Session
from src.domain.chatbot import ChatbotRepository, ChatbotMessageRepository, ChatbotIndexRepository, ChatbotVectorRepository
from src.infrastructure.database.rdb import get_psql_session, ChatbotRepositoryImpl, ChatbotMessageRepositoryImpl, ChatbotIndexRepositoryImpl
from src.infrastructure.database.vector import get_qdrant_session, QdrantClient, ChatbotVectorRepositoryImpl

def implement_chatbot_repository(session: Session = Depends(get_psql_session)) -> ChatbotRepository:
    return ChatbotRepositoryImpl(session)

def implement_chatbot_message_repository(session: Session = Depends(get_psql_session)) -> ChatbotMessageRepository:
    return ChatbotMessageRepositoryImpl(session)

def implement_chatbot_index_repository(session: Session = Depends(get_psql_session)) -> ChatbotIndexRepository:
    return ChatbotIndexRepositoryImpl(session)

def implement_chatbot_vector_repository(qdrant: QdrantClient = Depends(get_qdrant_session)) -> ChatbotVectorRepository:
    return ChatbotVectorRepositoryImpl(qdrant)


