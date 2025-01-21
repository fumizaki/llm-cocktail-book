from fastapi import Depends
from sqlalchemy.orm import Session
from src.domain.llm import LLMUsageRepository
from src.infrastructure.database.rdb.postgresql.repository.llm_usage import LLMUsageRepositoryImpl
from src.infrastructure.database.rdb.postgresql.session import get_rdb_session


def implement_llm_usage_repository(session: Session = Depends(get_rdb_session)) -> LLMUsageRepository:
    return LLMUsageRepositoryImpl(session)
