from datetime import datetime
import pytest
from sqlalchemy.orm import Session
from src.infrastructure.database.rdb import (
    AccountTable,
    ChatbotTable,
    ChatbotMessageTable
)

ACCOUNT_ID = "test-account-id"
EMAIL = "test@test.com"
PASSWORD = "P@ssW0rd123"
CHATBOT_ID = "test-chatbot-id"


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


def insert_chatbot(session: Session) -> None:
    try:
        _list = [
            ChatbotTable(
                id=CHATBOT_ID,
                account_id=ACCOUNT_ID,
                title="test-chatbot",
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
    insert_chatbot(session)