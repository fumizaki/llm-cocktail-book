from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.engine.row import Row, Tuple
from src.domain.entity.account import Account
from src.domain.repository.account import AccountRepository
from src.infrastructure.database.rdb.postgresql.schema.table import AccountTable


class AccountRepositoryImpl(AccountRepository):

    def __init__(self, session: Session) -> None:
        self._session = session

    @staticmethod
    def to_table(entity: Account) -> AccountTable:
        return AccountTable(
            **entity.model_dump()
        )
    
    @staticmethod
    def to_entity(obj: AccountTable) -> Account:
        return Account(
            id=str(obj.id),
            email=obj.email,
            email_verified=obj.email_verified,
            created_at=obj.created_at,
            updated_at=obj.updated_at,
            deleted_at=obj.deleted_at
        )


    def get_exclude_deleted(self, id: str) -> Account:
        result = self._session.execute(
            select(
                AccountTable
            )
            .filter(
                AccountTable.id == id,
                AccountTable.deleted_at == None
            )
        )
        row: Row[Tuple[AccountTable]] = result.one()
        return self.to_entity(row[0])
    

    def create(self, entity: Account) -> Account:
        obj = self.to_table(entity)
        self._session.add(obj)
        self._session.flush()
        return self.to_entity(obj)
    

    def verify(self, id: str, verified_at: datetime) -> Account:
        result = self._session.execute(
            select(
                AccountTable
            )
            .filter(
                AccountTable.id == id,
                AccountTable.deleted_at == None
            )
        )
        row: Row[Tuple[AccountTable]] = result.one()
        _in_db: AccountTable = row[0]
        _in_db.email_verified = verified_at
        self._session.flush()

        return self.to_entity(_in_db)
    

    def update(self) -> Account:
        pass
    

    def delete(self, id: str) -> Account:
        result = self._session.execute(
            select(
                AccountTable
            )
            .filter(
                AccountTable.id == id,
                AccountTable.deleted_at == None
            )
        )
        row: Row[Tuple[AccountTable]] = result.one()
        _in_db: AccountTable = row[0]
        _in_db.deleted_at = _in_db.now()
        self._session.flush()

        return self.to_entity(_in_db)
    
    
