from fastapi import Depends
from sqlalchemy.orm import Session
from src.presentation.dependency.query.account import implement_account_query
from src.presentation.dependency.repository import (
    implement_account_repository,
    implement_account_secret_repository
)
from src.application.oauth import OAuthSignupUsecase, OAuthPasswordUsecase, OAuthRefreshUsecase
from src.domain.query.account import AccountQuery
from src.domain.repository.account import AccountRepository
from src.domain.repository.account_secret import AccountSecretRepository
from src.infrastructure.database.rdb.postgresql.session import get_rdb_session
from src.infrastructure.database.rdb.transaction import TransactionClient
from src.infrastructure.resend.mailer import ResendEmailClient
from src.infrastructure.database.kvs.redis.session import RedisSessionClient

def implement_oauth_signup_usecase(
        session: Session = Depends(get_rdb_session),
        account_repository: AccountRepository = Depends(implement_account_repository),
        account_secret_repository: AccountSecretRepository = Depends(implement_account_secret_repository),
    ) -> OAuthSignupUsecase:
    return OAuthSignupUsecase(
        ResendEmailClient(),
        RedisSessionClient(),
        TransactionClient(session),
        account_repository,
        account_secret_repository
    )


def implement_oauth_password_usecase(
        account_query: AccountQuery = Depends(implement_account_query)
    ) -> OAuthPasswordUsecase:
    return OAuthPasswordUsecase(account_query)


def implement_oauth_refresh_usecase(
        account_repository: AccountRepository = Depends(implement_account_repository)
    ) -> OAuthRefreshUsecase:
    return OAuthRefreshUsecase(account_repository)