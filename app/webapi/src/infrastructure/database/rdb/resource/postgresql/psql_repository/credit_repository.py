from ..psql_table import CreditTable
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.engine.row import Row, Tuple, Sequence
from src.domain.credit import Credit, CreditRepository



class CreditRepositoryImpl(CreditRepository):

    def __init__(self, session: Session) -> None:
        self._session = session

    @staticmethod
    def to_table(entity: Credit) -> CreditTable:
        return CreditTable(
            **entity.model_dump()
        )
    
    @staticmethod
    def to_entity(obj: CreditTable) -> Credit:
        return Credit(
            id=str(obj.id),
            account_id=obj.account_id,
            balance=obj.balance,
            created_at=obj.created_at,
            updated_at=obj.updated_at,
            deleted_at=obj.deleted_at
        )


    def get_exclude_deleted(self, id: str) -> Credit:
        result = self._session.execute(
            select(
                CreditTable
            )
            .filter(
                CreditTable.id == id,
                CreditTable.deleted_at == None
            )
        )
        row: Row[Tuple[CreditTable]] = result.one()
        return self.to_entity(row[0])
    

    def get_all_exclude_deleted(self, account_id: str) -> list[Credit]:
        result = self._session.execute(
            select(
                CreditTable
            )
            .filter(
                CreditTable.account_id == account_id,
                CreditTable.deleted_at == None
            )
            .order_by(CreditTable.created_at.desc())
        )
        rows: Sequence[Row[Tuple[CreditTable]]] = result.all()
        return [self.to_entity(row[0]) for row in rows]


    def create(self, entity: Credit) -> Credit:
        obj = self.to_table(entity)
        self._session.add(obj)
        self._session.flush()
        return self.to_entity(obj)
    

    def update(self, id: str, balance: int) -> Credit:
        result = self._session.execute(
            select(
                CreditTable
            )
            .filter(
                CreditTable.id == id,
                CreditTable.deleted_at == None
            )
        )
        row: Row[Tuple[CreditTable]] = result.one()
        _in_db: CreditTable = row[0]
        _in_db.balance = balance
        self._session.flush()

        return self.to_entity(_in_db)
    

    def delete(self, id: str) -> Credit:
        result = self._session.execute(
            select(
                CreditTable
            )
            .filter(
                CreditTable.id == id,
                CreditTable.deleted_at == None
            )
        )
        row: Row[Tuple[CreditTable]] = result.one()
        _in_db: CreditTable = row[0]
        _in_db.deleted_at = _in_db.now()
        self._session.flush()

        return self.to_entity(_in_db)
    
    
