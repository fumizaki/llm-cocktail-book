from typing import Generator
import pytest
from sqlalchemy.orm import Session
from src.infrastructure.database.rdb import *
from src.infrastructure.database.rdb.resource.postgresql.psql_session import session_local


@pytest.fixture
def session() -> Generator[Session, None, None]:
    try:
        session = session_local()
        yield session

    finally:
        session.close()

@pytest.fixture
def trancate(session: Session) -> None:
    try:
        print('INFO: テーブルのデータを削除します')
        session.query(ChatbotMessageTable).delete()
        session.query(ChatbotTable).delete()
        session.query(AccountSecretTable).delete()
        session.query(AccountTable).delete()

    except Exception as e:
        print('ERROR: {}'.format(e))
        session.rollback()