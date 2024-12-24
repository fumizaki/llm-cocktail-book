from fastapi import Depends, Header
from sqlalchemy.orm import Session
from src.domain.repository.account import AccountRepository
from src.domain.repository.account_secret import AccountSecretRepository
from src.infrastructure.database.rdb.postgresql.repository.account import AccountRepositoryImpl
from src.infrastructure.database.rdb.postgresql.repository.account_secret import AccountSecretRepositoryImpl
from src.infrastructure.database.rdb.postgresql.session import get_rdb_session


def implement_account_repository(session: Session = Depends(get_rdb_session)) -> AccountRepository:
    return AccountRepositoryImpl(session)

def implement_account_secret_repository(session: Session = Depends(get_rdb_session)) -> AccountSecretRepository:
    return AccountSecretRepositoryImpl(session)

