from ..psql_table import CreditTransactionTable
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.engine.row import Row, Tuple, Sequence
from src.domain.credit import CreditTransaction, CreditTransactionRepository



class CreditTransactionRepositoryImpl(CreditTransactionRepository):

    def __init__(self, session: Session) -> None:
        self._session = session

    @staticmethod
    def to_table(entity: CreditTransaction) -> CreditTransactionTable:
        return CreditTransactionTable(
            **entity.model_dump()
        )
    
    @staticmethod
    def to_entity(obj: CreditTransactionTable) -> CreditTransaction:
        return CreditTransaction(
            id=str(obj.id),
            account_id=obj.account_id,
            transaction_type=obj.transaction_type,
            credit=obj.credit,
            description=obj.description,
            created_at=obj.created_at,
            updated_at=obj.updated_at,
            deleted_at=obj.deleted_at
        )


    def get_exclude_deleted(self, id: str) -> CreditTransaction:
        result = self._session.execute(
            select(
                CreditTransactionTable
            )
            .filter(
                CreditTransactionTable.id == id,
                CreditTransactionTable.deleted_at == None
            )
        )
        row: Row[Tuple[CreditTransactionTable]] = result.one()
        return self.to_entity(row[0])
    

    def get_all_exclude_deleted(self, account_id: str) -> list[CreditTransaction]:
        result = self._session.execute(
            select(
                CreditTransactionTable
            )
            .filter(
                CreditTransactionTable.account_id == account_id,
                CreditTransactionTable.deleted_at == None
            )
            .order_by(CreditTransactionTable.created_at.desc())
        )
        rows: Sequence[Row[Tuple[CreditTransactionTable]]] = result.all()
        return [self.to_entity(row[0]) for row in rows]
    


    def create(self, entity: CreditTransaction) -> CreditTransaction:
        obj = self.to_table(entity)
        self._session.add(obj)
        self._session.flush()
        return self.to_entity(obj)
    

    def delete(self, id: str) -> CreditTransaction:
        result = self._session.execute(
            select(
                CreditTransactionTable
            )
            .filter(
                CreditTransactionTable.id == id,
                CreditTransactionTable.deleted_at == None
            )
        )
        row: Row[Tuple[CreditTransactionTable]] = result.one()
        _in_db: CreditTransactionTable = row[0]
        _in_db.deleted_at = _in_db.now()
        self._session.flush()

        return self.to_entity(_in_db)
    
    
