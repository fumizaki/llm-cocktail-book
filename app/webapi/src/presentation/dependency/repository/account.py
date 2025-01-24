from fastapi import Depends
from sqlalchemy.orm import Session
from src.domain.account import AccountRepository, AccountSecretRepository
from src.infrastructure.database.rdb import get_psql_session, AccountRepositoryImpl, AccountSecretRepositoryImpl



def implement_account_repository(session: Session = Depends(get_psql_session)) -> AccountRepository:
    return AccountRepositoryImpl(session)

def implement_account_secret_repository(session: Session = Depends(get_psql_session)) -> AccountSecretRepository:
    return AccountSecretRepositoryImpl(session)

