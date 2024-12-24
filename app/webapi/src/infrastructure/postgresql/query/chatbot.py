from sqlalchemy.orm import Session
from sqlalchemy.orm import selectinload
from src.application.chatbot.message.query import ChatbotMessageQuery
from src.domain.entity.chatbot_message import ChatbotMessage
from src.domain.aggregate.chatbot import AggChatbot
from src.infrastructure.postgresql.schema.table import (
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

        messages = list[ChatbotMessage] = []
        for message in chatbot.messages:
            if message.deleted_at is not None:
                continue
            messages.append(
                ChatbotMessage(
                    **message
                )
            )

        return AggChatbot(
            id=chatbot.id,
            title=chatbot.title,
            created_at=chatbot.created_at,
            updated_at=chatbot.updated_at,
            messages=messages
        )