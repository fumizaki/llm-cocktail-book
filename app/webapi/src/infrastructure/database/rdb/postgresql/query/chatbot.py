from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload, contains_eager
from src.application.chatbot.message.query import ChatbotMessageQuery
from src.domain.entity.chatbot_message import ChatbotMessage
from src.domain.aggregate.chatbot import AggChatbot
from src.infrastructure.database.rdb.postgresql.schema.table import (
    ChatbotTable,
    ChatbotMessageTable
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
    
    def get_agg_chatbot_limited(self, chatbot_id: str, account_id: str, limit: int) -> AggChatbot:
        # メッセージの最新N件を取得するサブクエリ
        latest_messages = (
            select(ChatbotMessageTable)
            .filter(
                ChatbotMessageTable.chatbot_id == chatbot_id,
                ChatbotMessageTable.deleted_at == None
            )
            .order_by(ChatbotMessageTable.created_at.desc())
            .limit(limit)
            .subquery()
            )

        # チャットボットとメッセージを外部結合
        chatbot = (
            self._session.query(ChatbotTable)
            .outerjoin(latest_messages, ChatbotTable.id == latest_messages.c.chatbot_id)
            .filter(
                ChatbotTable.id == chatbot_id,
                ChatbotTable.account_id == account_id,
                ChatbotTable.deleted_at == None
            )
            .options(contains_eager(ChatbotTable.messages, alias=latest_messages))
            .first()
        )

        if not chatbot:
            raise Exception("Chatbot not found")
        
        messages = [
            ChatbotMessage(
                id=str(message.id),
                chatbot_id=message.chatbot_id,
                role=message.role,
                content=message.content,
                created_at=message.created_at,
                updated_at=message.updated_at,
                deleted_at=message.deleted_at
            )
            for message in chatbot.messages
        ]

        return AggChatbot(
            id=chatbot.id,
            account_id=chatbot.account_id,
            title=chatbot.title,
            created_at=chatbot.created_at,
            updated_at=chatbot.updated_at,
            messages=messages
        )