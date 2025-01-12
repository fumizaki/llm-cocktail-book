import pytest
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
    ]
)   
def test_all(session, expected, account_id):
    r = ChatbotRepositoryImpl(session)
    result = r.get_all_exclude_deleted(account_id)
    assert isinstance(result, expected)
