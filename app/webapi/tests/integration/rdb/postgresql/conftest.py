import pytest
from sqlalchemy.orm import Session
from src.infrastructure.database.rdb.postgresql.session import session_local

@pytest.fixture
def session() -> Session:
    return session_local()
