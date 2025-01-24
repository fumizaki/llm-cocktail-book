from fastapi import Depends
from sqlalchemy.orm import Session
from src.presentation.dependency.authorization import get_credential_from_header
from src.presentation.dependency.repository.chatbot import implement_chatbot_repository, implement_chatbot_message_repository
from src.presentation.dependency.repository.llm_usage import implement_llm_usage_repository
from src.presentation.dependency.query.chatbot import implement_chatbot_query
from src.application.chatbot import ChatbotUsecase, ChatbotMessageUsecase, ChatbotQuery
from src.application.credential import Credential
from src.domain.chatbot import ChatbotRepository, ChatbotMessageRepository
from src.domain.llm import LLMUsageRepository
from src.infrastructure.database.rdb import get_psql_session, TransactionClient


def implement_chatbot_usecase(
        credential: Credential = Depends(get_credential_from_header),
        session: Session = Depends(get_psql_session),
        chatbot_repository: ChatbotRepository = Depends(implement_chatbot_repository)
    ):
    return ChatbotUsecase(
        credential,
        TransactionClient(session),
        chatbot_repository
        )

def implement_chatbot_message_usecase(
       credential: Credential = Depends(get_credential_from_header),
       session: Session = Depends(get_psql_session),
       chatbot_query: ChatbotQuery = Depends(implement_chatbot_query),
       chatbot_message_repository: ChatbotMessageRepository = Depends(implement_chatbot_message_repository),
       llm_usage_repository: LLMUsageRepository = Depends(implement_llm_usage_repository)
    ):
    return ChatbotMessageUsecase(
        credential,
        TransactionClient(session),
        chatbot_query,
        chatbot_message_repository,
        llm_usage_repository
        )