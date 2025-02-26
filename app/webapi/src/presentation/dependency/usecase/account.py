from fastapi import Depends
from sqlalchemy.orm import Session
from src.presentation.dependency.authorization import get_credential_from_header
from src.presentation.dependency.repository.account import (
    implement_account_repository,
    implement_account_secret_repository
)
from src.application.account import AccountSecretUsecase
from src.domain.account import AccountCredentialModel, AccountRepository, AccountSecretRepository
from src.infrastructure.database.rdb import get_psql_session, TransactionClient
from src.infrastructure.email.resource import ResendEmailClient



def implement_profile_usecase(
        session: Session = Depends(get_psql_session),
        account_repository: AccountRepository = Depends(implement_account_repository),
    ):
    return


def implement_secret_usecase(
        credential: AccountCredentialModel = Depends(get_credential_from_header),
        session: Session = Depends(get_psql_session),
        account_secret_repository: AccountSecretRepository = Depends(implement_account_secret_repository),
    ):
    return AccountSecretUsecase(
        ResendEmailClient(),
        credential,
        TransactionClient(session),
        account_secret_repository
        )