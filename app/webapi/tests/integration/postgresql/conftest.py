from typing import Generator
import pytest
from sqlalchemy.orm import Session
from src.infrastructure.postgresql.session import get_rdb_session

@pytest.fixture
def rdb() -> Generator[Session, None, None]:
    return get_rdb_session()

