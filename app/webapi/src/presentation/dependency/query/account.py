from fastapi import Depends, Header
from sqlalchemy.orm import Session
from src.application.account.query import AccountQuery
from src.infrastructure.database.rdb.postgresql.query.account import AccountQueryImpl
from src.infrastructure.database.rdb.postgresql.session import get_rdb_session


def implement_account_query(session: Session = Depends(get_rdb_session)) -> AccountQuery:
    return AccountQueryImpl(session)

