from fastapi import HTTPException, status
from .account_secret_model import UpdateAccountSecretModel
from ..credential import Credential
from src.domain.account import AccountSecret, AccountSecretRepository
from src.infrastructure.database.rdb import TransactionClient
from src.infrastructure.hashing import HashingClient
from src.infrastructure.email import EmailClient, EmailModel, build_update_password_content

class AccountSecretUsecase:
    def __init__(
        self,
        mailer: EmailClient,
        credential: Credential,
        tx: TransactionClient,
        account_secret_repository: AccountSecretRepository,
    ) -> None:
        self.mailer = mailer
        self.credential = credential
        self.tx = tx
        self.account_secret_repository = account_secret_repository


    def update_exec(self, params: UpdateAccountSecretModel) -> None:
        try:
            if params.current_password == params.new_password:
                raise Exception
            
            account_secret_in_db: AccountSecret = self.account_secret_repository.get_exclude_deleted(self.credential.account_id)
            if not HashingClient.verify(account_secret_in_db.password, params.current_password, account_secret_in_db.salt, account_secret_in_db.stretching):
                raise Exception
            
            hasher = HashingClient()
            self.account_secret_repository.update(
                account_secret_in_db.id,
                HashingClient.hash(params.new_password),
                hasher.salt,
                hasher.stretching
                )
            # メール送信
            self.mailer.send(
                params=EmailModel(
                    to=[self.credential.email],
                    **build_update_password_content().model_dump()
                )
            )

            self.tx.commit()

        except Exception as e:
            self.tx.rollback()

