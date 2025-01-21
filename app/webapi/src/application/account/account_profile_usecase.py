from datetime import datetime
from fastapi import HTTPException, status
from src.domain.account import Account
from src.domain.repository.account import AccountRepository
from src.infrastructure.database.rdb.transaction import TransactionClient

class AccountProfileUsecase:
    def __init__(
        self,
        tx: TransactionClient,
        account_repository: AccountRepository,
    ) -> None:
        self.tx = tx
        self.account_repository = account_repository


    def get_exec() -> Account:
        return