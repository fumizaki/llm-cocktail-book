import pytest
from src.domain.entity.chatbot import Chatbot
from src.domain.repository.chatbot import ChatbotRepository
from src.infrastructure.database.rdb.postgresql.repository.chatbot import ChatbotRepositoryImpl


class NotImplemented(ChatbotRepository):
    pass

def test_not_implemented():
    with pytest.raises(TypeError):
        NotImplemented()



@pytest.mark.parametrize(
    "expected, account_id",
    [
        (list, ""),
        (list, "test-account-id")
    ]
)   
def test_case001_get_all(session, setup, expected, account_id):
    r = ChatbotRepositoryImpl(session)
    result = r.get_all_exclude_deleted(account_id)
    assert isinstance(result, expected)

@pytest.mark.parametrize(
    "expected, chatbot_id",
    [
        (Chatbot, "test-chatbot-id")
    ]
)   
def test_case002_get(session, setup, expected, chatbot_id):
    r = ChatbotRepositoryImpl(session)
    result = r.get_exclude_deleted(chatbot_id)
    assert isinstance(result, expected)


