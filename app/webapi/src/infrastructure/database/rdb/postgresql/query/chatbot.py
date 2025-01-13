from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload
from src.application.chatbot.message.query import ChatbotMessageQuery
from src.domain.entity.chatbot_message import ChatbotMessage
from src.domain.aggregate.chatbot import AggChatbot
from src.infrastructure.database.rdb.postgresql.schema.table import (
    ChatbotTable,
)
class ChatbotMessageQueryImpl(ChatbotMessageQuery):
    def __init__(self, session: Session) -> None:
        self._session = session

    def get_agg_chatbot(self, chatbot_id: str, account_id: str) -> AggChatbot:
        chatbot = (
            self._session.query(ChatbotTable)
            .options(selectinload(ChatbotTable.messages))
            .filter(ChatbotTable.id == chatbot_id, ChatbotTable.account_id == account_id, ChatbotTable.deleted_at == None)
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
    