from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.engine.row import Row, Tuple
from src.domain.entity.account_secret import AccountSecret
from src.domain.repository.account_secret import AccountSecretRepository
from src.infrastructure.postgresql.schema.table import AccountSecretTable


class AccountSecretRepositoryImpl(AccountSecretRepository):

    def __init__(self, session: Session) -> None:
        self._session = session
    
    @staticmethod
    def to_table(entity: AccountSecret) -> AccountSecretTable:
        return AccountSecretTable(
            **entity.model_dump()
        )
    
    @staticmethod
    def to_entity(obj: AccountSecretTable) -> AccountSecret:
        return AccountSecret(
            id=str(obj.id),
            account_id=str(obj.account_id),
            password=obj.password,
            salt=obj.salt,
            stretching=obj.stretching,
            created_at=obj.created_at,
            updated_at=obj.updated_at,
            deleted_at=obj.deleted_at
        )


    def get_exclude_deleted(self, account_id: str) -> AccountSecret:
        result = self._session.execute(
            select(
                AccountSecretTable
            )
            .filter(
                AccountSecretTable.account_id == account_id,
                AccountSecretTable.deleted_at == None
            )
        )
        row: Row[Tuple[AccountSecretTable]] = result.one()
        return self.to_entity(row[0])
    

    def create(self, entity: AccountSecret) -> AccountSecret:
        obj = self.to_table(entity)
        self._session.add(obj)
        self._session.flush()
        return self.to_entity(obj)
    
    
    def update(self, id: str, password: str, salt: str, stretching: int) -> AccountSecret:
        result = self._session.execute(
            select(
                AccountSecretTable
            )
            .filter(
                AccountSecretTable.id == id,
                AccountSecretTable.deleted_at == None
            )
        )
        row: Row[Tuple[AccountSecretTable]] = result.one()
        _in_db: AccountSecretTable = row[0]
        _in_db.password = password
        _in_db.salt = salt
        _in_db.stretching = stretching
        self._session.flush()

        return self.to_entity(_in_db)
    

    def delete(self, id: str) -> AccountSecret:
        result = self._session.execute(
            select(
                AccountSecretTable
            )
            .filter(
                AccountSecretTable.id == id,
                AccountSecretTable.deleted_at == None
            )
        )
        row: Row[Tuple[AccountSecretTable]] = result.one()
        _in_db: AccountSecretTable = row[0]
        _in_db.deleted_at = _in_db.now()
        self._session.flush()

        return self.to_entity(_in_db)
    
    
