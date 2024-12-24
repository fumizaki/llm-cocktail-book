from fastapi import Depends
from sqlalchemy.orm import Session
from src.presentation.dependency.authorization import get_credential_from_header
from src.presentation.dependency.repository import (
    implement_account_repository,
    implement_account_secret_repository
)
from src.application.account.secret import AccountSecretUsecase
from src.domain.entity.credential import Credential
from src.domain.repository.account import AccountRepository
from src.domain.repository.account_secret import AccountSecretRepository
from src.infrastructure.database.rdb.postgresql.session import get_rdb_session
from src.infrastructure.database.rdb.transaction import TransactionClient
from src.infrastructure.resend.mailer import ResendEmailClient



def implement_profile_usecase(
        session: Session = Depends(get_rdb_session),
        account_repository: AccountRepository = Depends(implement_account_repository),
    ):
    return


def implement_secret_usecase(
        credential: Credential = Depends(get_credential_from_header),
        session: Session = Depends(get_rdb_session),
        account_secret_repository: AccountSecretRepository = Depends(implement_account_secret_repository),
    ):
    return AccountSecretUsecase(
        ResendEmailClient(),
        credential,
        TransactionClient(session),
        account_secret_repository
        )