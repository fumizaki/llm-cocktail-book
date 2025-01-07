from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.engine.row import Row, Tuple, Sequence
from src.domain.entity.chatbot_message import ChatbotMessage
from src.domain.repository.chatbot_message import ChatbotMessageRepository
from src.infrastructure.database.rdb.postgresql.schema.table import ChatbotMessageTable


class ChatbotMessageRepositoryImpl(ChatbotMessageRepository):

    def __init__(self, session: Session) -> None:
        self._session = session

    @staticmethod
    def to_table(entity: ChatbotMessage) -> ChatbotMessageTable:
        return ChatbotMessageTable(
            **entity.model_dump()
        )
    
    @staticmethod
    def to_entity(obj: ChatbotMessageTable) -> ChatbotMessage:
        return ChatbotMessage(
            id=str(obj.id),
            chatbot_id=obj.chatbot_id,
            role=obj.role,
            content=obj.content,
            created_at=obj.created_at,
            updated_at=obj.updated_at,
            deleted_at=obj.deleted_at
        )


    def get_exclude_deleted(self, id: str) -> ChatbotMessage:
        result = self._session.execute(
            select(
                ChatbotMessageTable
            )
            .filter(
                ChatbotMessageTable.id == id,
                ChatbotMessageTable.deleted_at == None
            )
        )
        row: Row[Tuple[ChatbotMessageTable]] = result.one()
        return self.to_entity(row[0])
    

    def get_all_exclude_deleted(self, chatbot_id: str) -> list[ChatbotMessage]:
        result = self._session.execute(
            select(
                ChatbotMessageTable
            )
            .filter(
                ChatbotMessageTable.chatbot_id == chatbot_id,
                ChatbotMessageTable.deleted_at == None
            )
        )
        rows: Sequence[Row[Tuple[ChatbotMessageTable]]] = result.all()
        return [self.to_entity(row[0]) for row in rows]


    def create(self, entity: ChatbotMessage) -> ChatbotMessage:
        obj = self.to_table(entity)
        self._session.add(obj)
        self._session.flush()
        return self.to_entity(obj)
    

    def update(self) -> ChatbotMessage:
        pass
    

    def delete(self, id: str) -> ChatbotMessage:
        result = self._session.execute(
            select(
                ChatbotMessageTable
            )
            .filter(
                ChatbotMessageTable.id == id,
                ChatbotMessageTable.deleted_at == None
            )
        )
        row: Row[Tuple[ChatbotMessageTable]] = result.one()
        _in_db: ChatbotMessageTable = row[0]
        _in_db.deleted_at = _in_db.now()
        self._session.flush()

        return self.to_entity(_in_db)
    
    
