from ..psql_table import ChatbotTable
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.engine.row import Row, Tuple, Sequence
from src.domain.chatbot import Chatbot, ChatbotRepository



class ChatbotRepositoryImpl(ChatbotRepository):

    def __init__(self, session: Session) -> None:
        self._session = session

    @staticmethod
    def to_table(entity: Chatbot) -> ChatbotTable:
        return ChatbotTable(
            **entity.model_dump()
        )
    
    @staticmethod
    def to_entity(obj: ChatbotTable) -> Chatbot:
        return Chatbot(
            id=str(obj.id),
            account_id=obj.account_id,
            title=obj.title,
            created_at=obj.created_at,
            updated_at=obj.updated_at,
            deleted_at=obj.deleted_at
        )


    def get_exclude_deleted(self, id: str) -> Chatbot:
        result = self._session.execute(
            select(
                ChatbotTable
            )
            .filter(
                ChatbotTable.id == id,
                ChatbotTable.deleted_at == None
            )
        )
        row: Row[Tuple[ChatbotTable]] = result.one()
        return self.to_entity(row[0])
    

    def get_all_exclude_deleted(self, account_id: str) -> list[Chatbot]:
        result = self._session.execute(
            select(
                ChatbotTable
            )
            .filter(
                ChatbotTable.account_id == account_id,
                ChatbotTable.deleted_at == None
            )
            .order_by(ChatbotTable.created_at.desc())
        )
        rows: Sequence[Row[Tuple[ChatbotTable]]] = result.all()
        return [self.to_entity(row[0]) for row in rows]


    def create(self, entity: Chatbot) -> Chatbot:
        obj = self.to_table(entity)
        self._session.add(obj)
        self._session.flush()
        return self.to_entity(obj)
    

    def update(self) -> Chatbot:
        pass
    

    def delete(self, id: str) -> Chatbot:
        result = self._session.execute(
            select(
                ChatbotTable
            )
            .filter(
                ChatbotTable.id == id,
                ChatbotTable.deleted_at == None
            )
        )
        row: Row[Tuple[ChatbotTable]] = result.one()
        _in_db: ChatbotTable = row[0]
        _in_db.deleted_at = _in_db.now()
        self._session.flush()

        return self.to_entity(_in_db)
    
    
