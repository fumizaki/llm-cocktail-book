from sqlalchemy.orm import Session
from sqlalchemy.orm import selectinload
from src.application.account import AccountQuery
from src.domain.account import AccountWithSecret, AccountSecret
from ..psql_table import (
    AccountTable,
)


class AccountQueryImpl(AccountQuery):

    def __init__(self, session: Session) -> None:
        self._session = session

    def get_account_with_secret(self, email: str) -> AccountWithSecret:

        account = (
            self._session.query(AccountTable)
            .options(selectinload(AccountTable.secret))
            .filter(AccountTable.email == email, AccountTable.email_verified != None, AccountTable.deleted_at == None)
            .one()
        )

        return AccountWithSecret(
            id=account.id,
            email=account.email,
            email_verified=account.email_verified,
            secret=AccountSecret(
                id=account.secret.id,
                account_id=account.secret.account_id,
                password=account.secret.password,
                salt=account.secret.salt,
                stretching=account.secret.stretching
            ),
        )


