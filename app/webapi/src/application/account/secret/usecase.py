from fastapi import HTTPException, status
from src.application.account.secret import UpdateAccountSecretModel
from src.domain.repository.account_secret import AccountSecretRepository
from src.domain.entity.credential import Credential
from src.domain.entity.account_secret import AccountSecret
from src.infrastructure.database.rdb.transaction import TransactionClient
from src.infrastructure.core.security.hash import HashClient
from src.infrastructure.core.email.mailer import EmailClient
from src.infrastructure.core.email.content import build_update_password_content

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
            
            account_secret_in_db: AccountSecret = self.account_secret_repository.get_exclude_deleted(self.credential.id)
            if not HashClient.verify(account_secret_in_db.password, params.current_password, account_secret_in_db.salt, account_secret_in_db.stretching):
                raise Exception
            
            salt = HashClient.create_salt()
            stretching = HashClient.create_stretching()
            self.account_secret_repository.update(
                account_secret_in_db.id,
                HashClient.hash(params.new_password, salt, stretching),
                salt,
                stretching
                )
            # メール送信
            self.mailer.send_mail(
                to_add=[self.credential.email],
                content=build_update_password_content()
            )

            self.tx.commit()

        except Exception as e:
            self.tx.rollback()

