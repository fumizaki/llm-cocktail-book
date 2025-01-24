from ..psql_table import LLMUsageTable
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.engine.row import Row, Tuple, Sequence
from src.domain.llm import LLMUsage, LLMUsageRepository



class LLMUsageRepositoryImpl(LLMUsageRepository):

    def __init__(self, session: Session) -> None:
        self._session = session

    @staticmethod
    def to_table(entity: LLMUsage) -> LLMUsageTable:
        return LLMUsageTable(
            **entity.model_dump()
        )
    
    @staticmethod
    def to_entity(obj: LLMUsageTable) -> LLMUsage:
        return LLMUsage(
            id=str(obj.id),
            account_id=obj.account_id,
            resource=obj.resource,
            model=obj.model,
            task=obj.task,
            usage=obj.usage,
            created_at=obj.created_at,
            updated_at=obj.updated_at,
            deleted_at=obj.deleted_at
        )


    def get_exclude_deleted(self, id: str) -> LLMUsage:
        result = self._session.execute(
            select(
                LLMUsageTable
            )
            .filter(
                LLMUsageTable.id == id,
                LLMUsageTable.deleted_at == None
            )
        )
        row: Row[Tuple[LLMUsageTable]] = result.one()
        return self.to_entity(row[0])
    

    def get_all_exclude_deleted(self, account_id: str) -> list[LLMUsage]:
        result = self._session.execute(
            select(
                LLMUsageTable
            )
            .filter(
                LLMUsageTable.account_id == account_id,
                LLMUsageTable.deleted_at == None
            )
            .order_by(LLMUsageTable.created_at.desc())
        )
        rows: Sequence[Row[Tuple[LLMUsageTable]]] = result.all()
        return [self.to_entity(row[0]) for row in rows]


    def create(self, entity: LLMUsage) -> LLMUsage:
        obj = self.to_table(entity)
        self._session.add(obj)
        self._session.flush()
        return self.to_entity(obj)
    

    def update(self) -> LLMUsage:
        pass
    

    def delete(self, id: str) -> LLMUsage:
        result = self._session.execute(
            select(
                LLMUsageTable
            )
            .filter(
                LLMUsageTable.id == id,
                LLMUsageTable.deleted_at == None
            )
        )
        row: Row[Tuple[LLMUsageTable]] = result.one()
        _in_db: LLMUsageTable = row[0]
        _in_db.deleted_at = _in_db.now()
        self._session.flush()

        return self.to_entity(_in_db)
    
    
