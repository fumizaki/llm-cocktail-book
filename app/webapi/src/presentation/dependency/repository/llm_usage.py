from fastapi import Depends
from sqlalchemy.orm import Session
from src.domain.llm import LLMUsageRepository
from src.infrastructure.database.rdb import get_psql_session, LLMUsageRepositoryImpl


def implement_llm_usage_repository(session: Session = Depends(get_psql_session)) -> LLMUsageRepository:
    return LLMUsageRepositoryImpl(session)
