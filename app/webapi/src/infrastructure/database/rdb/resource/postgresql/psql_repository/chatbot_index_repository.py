from ..psql_table import ChatbotIndexTable
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.engine.row import Row, Tuple, Sequence
from src.domain.chatbot import ChatbotIndex, ChatbotIndexRepository



class ChatbotIndexRepositoryImpl(ChatbotIndexRepository):

    def __init__(self, session: Session) -> None:
        self._session = session

    @staticmethod
    def to_table(entity: ChatbotIndex) -> ChatbotIndexTable:
        return ChatbotIndexTable(
            **entity.model_dump()
        )
    
    @staticmethod
    def to_entity(obj: ChatbotIndexTable) -> ChatbotIndex:
        return ChatbotIndex(
            id=str(obj.id),
            chatbot_id=obj.chatbot_id,
            content=obj.content,
            created_at=obj.created_at,
            updated_at=obj.updated_at,
            deleted_at=obj.deleted_at
        )


    def get_exclude_deleted(self, id: str) -> ChatbotIndex:
        result = self._session.execute(
            select(
                ChatbotIndexTable
            )
            .filter(
                ChatbotIndexTable.id == id,
                ChatbotIndexTable.deleted_at == None
            )
        )
        row: Row[Tuple[ChatbotIndexTable]] = result.one()
        return self.to_entity(row[0])
    

    def get_all_exclude_deleted(self, chatbot_id: str) -> list[ChatbotIndex]:
        result = self._session.execute(
            select(
                ChatbotIndexTable
            )
            .filter(
                ChatbotIndexTable.chatbot_id == chatbot_id,
                ChatbotIndexTable.deleted_at == None
            )
            .order_by(ChatbotIndexTable.created_at.desc())
        )
        rows: Sequence[Row[Tuple[ChatbotIndexTable]]] = result.all()
        return [self.to_entity(row[0]) for row in rows]
    

    def create(self, entity: ChatbotIndex) -> ChatbotIndex:
        obj = self.to_table(entity)
        self._session.add(obj)
        self._session.flush()
        return self.to_entity(obj)
    

    def update(self) -> ChatbotIndex:
        pass
    

    def delete(self, id: str) -> ChatbotIndex:
        result = self._session.execute(
            select(
                ChatbotIndexTable
            )
            .filter(
                ChatbotIndexTable.id == id,
                ChatbotIndexTable.deleted_at == None
            )
        )
        row: Row[Tuple[ChatbotIndexTable]] = result.one()
        _in_db: ChatbotIndexTable = row[0]
        _in_db.deleted_at = _in_db.now()
        self._session.flush()

        return self.to_entity(_in_db)
    
    
