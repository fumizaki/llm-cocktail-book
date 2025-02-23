from sqlalchemy.orm import Session, contains_eager
from src.application.chatbot import ChatbotQuery
from src.domain.chatbot import AggChatbot, ChatbotMessage
from ..psql_table import (
    ChatbotTable,
    ChatbotMessageTable
)
class ChatbotQueryImpl(ChatbotQuery):
    def __init__(self, session: Session) -> None:
        self._session = session
    
    def get_agg_chatbot(self, chatbot_id: str, account_id: str) -> AggChatbot:
        chatbot = (
            self._session.query(ChatbotTable)
            .join(ChatbotTable.messages, isouter=True)
            .options(contains_eager(ChatbotTable.messages))
            .filter(ChatbotTable.id == chatbot_id, ChatbotTable.account_id == account_id, ChatbotTable.deleted_at == None)
            .order_by(ChatbotMessageTable.created_at.asc())
            .one()
        )

        messages: list[ChatbotMessage] = []
        for message in chatbot.messages:
            if message.deleted_at is not None:
                continue
            messages.append(
                ChatbotMessage(
                    id=str(message.id),
                    chatbot_id=message.chatbot_id,
                    role=message.role,
                    content=message.content,
                    created_at=message.created_at,
                    updated_at=message.updated_at,
                    deleted_at=message.deleted_at
                )
            )

        return AggChatbot(
            id=chatbot.id,
            account_id=chatbot.account_id,
            title=chatbot.title,
            created_at=chatbot.created_at,
            updated_at=chatbot.updated_at,
            messages=messages
        )
    