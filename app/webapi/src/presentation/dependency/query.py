from fastapi import Depends, Header
from sqlalchemy.orm import Session
from src.domain.query.account import AccountQuery
from src.infrastructure.postgresql.query.account import AccountQueryImpl
from src.infrastructure.postgresql.session import get_rdb_session


def implement_account_query(session: Session = Depends(get_rdb_session)) -> AccountQuery:
    return AccountQueryImpl(session)

