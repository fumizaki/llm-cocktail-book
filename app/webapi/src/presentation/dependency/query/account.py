from fastapi import Depends, Header
from sqlalchemy.orm import Session
from src.application.account import AccountQuery
from src.infrastructure.database.rdb import get_psql_session, AccountQueryImpl


def implement_account_query(session: Session = Depends(get_psql_session)) -> AccountQuery:
    return AccountQueryImpl(session)

