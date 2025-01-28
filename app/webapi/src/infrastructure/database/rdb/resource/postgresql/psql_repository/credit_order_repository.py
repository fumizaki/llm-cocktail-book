from ..psql_table import CreditOrderTable
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.engine.row import Row, Tuple, Sequence
from src.domain.credit import CreditOrder, CreditOrderRepository



class CreditOrderRepositoryImpl(CreditOrderRepository):

    def __init__(self, session: Session) -> None:
        self._session = session

    @staticmethod
    def to_table(entity: CreditOrder) -> CreditOrderTable:
        return CreditOrderTable(
            **entity.model_dump()
        )
    
    @staticmethod
    def to_entity(obj: CreditOrderTable) -> CreditOrder:
        return CreditOrder(
            id=str(obj.id),
            account_id=obj.account_id,
            provider=obj.provider,
            reference_id=obj.reference_id,
            credit=obj.credit,
            amount=obj.amount,
            currency=obj.currency,
            status=obj.status,
            created_at=obj.created_at,
            updated_at=obj.updated_at,
            deleted_at=obj.deleted_at
        )


    def get_exclude_deleted(self, id: str) -> CreditOrder:
        result = self._session.execute(
            select(
                CreditOrderTable
            )
            .filter(
                CreditOrderTable.id == id,
                CreditOrderTable.deleted_at == None
            )
        )
        row: Row[Tuple[CreditOrderTable]] = result.one()
        return self.to_entity(row[0])
    

    def get_all_exclude_deleted(self, account_id: str) -> list[CreditOrder]:
        result = self._session.execute(
            select(
                CreditOrderTable
            )
            .filter(
                CreditOrderTable.account_id == account_id,
                CreditOrderTable.deleted_at == None
            )
            .order_by(CreditOrderTable.created_at.desc())
        )
        rows: Sequence[Row[Tuple[CreditOrderTable]]] = result.all()
        return [self.to_entity(row[0]) for row in rows]
    


    def create(self, entity: CreditOrder) -> CreditOrder:
        obj = self.to_table(entity)
        self._session.add(obj)
        self._session.flush()
        return self.to_entity(obj)
    

    def update(self, id: str, status: str) -> CreditOrder:
        result = self._session.execute(
            select(
                CreditOrderTable
            )
            .filter(
                CreditOrderTable.id == id,
                CreditOrderTable.deleted_at == None
            )
        )
        row: Row[Tuple[CreditOrderTable]] = result.one()
        _in_db: CreditOrderTable = row[0]
        _in_db.status = status
        self._session.flush()

        return self.to_entity(_in_db)   


    def delete(self, id: str) -> CreditOrder:
        result = self._session.execute(
            select(
                CreditOrderTable
            )
            .filter(
                CreditOrderTable.id == id,
                CreditOrderTable.deleted_at == None
            )
        )
        row: Row[Tuple[CreditOrderTable]] = result.one()
        _in_db: CreditOrderTable = row[0]
        _in_db.deleted_at = _in_db.now()
        self._session.flush()

        return self.to_entity(_in_db)
    
    
