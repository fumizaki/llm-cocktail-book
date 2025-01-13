from datetime import datetime
import pytest
from sqlalchemy.orm import Session
from src.infrastructure.database.rdb.postgresql import (
    AccountTable,
    AccountSecretTable
)
from src.infrastructure.hashing import HashingClient

ACCOUNT_ID = "test-account-id"
EMAIL = "test@test.com"
PASSWORD = "P@ssw0rd123"


def insert_account(session: Session) -> None:
    try:
        _list = [
            AccountTable(
                id=ACCOUNT_ID,
                email=EMAIL,
                email_verified=datetime.now()
            )
        ]
        session.add_all(_list)
        session.flush()

        session.commit()

    except Exception as e:
        print('ERROR: {}'.format(e))
        session.rollback()

def insert_account_secret(session: Session) -> None:
    try:
        hashing_client = HashingClient()

        _list = [
            AccountSecretTable(
                id="test-account-secret-id",
                account_id=ACCOUNT_ID,
                password=hashing_client.hash(PASSWORD),
                salt=hashing_client.salt,
                stretching=hashing_client.stretching
            )
        ]
        session.add_all(_list)
        session.flush()

        session.commit()

    except Exception as e:
        print('ERROR: {}'.format(e))
        session.rollback()


@pytest.fixture(scope="function")
def setup(session: Session, trancate: None) -> None:
    print('INFO: テーブルにデータを挿入します')
    insert_account(session)
    insert_account_secret(session)