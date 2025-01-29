from fastapi import Depends
from sqlalchemy.orm import Session
from src.presentation.dependency.query.account import implement_account_query
from src.presentation.dependency.repository.account import (
    implement_account_repository,
    implement_account_secret_repository
)
from src.presentation.dependency.repository.credit import implement_credit_repository
from src.application.oauth import OAuthSignupUsecase, OAuthPasswordUsecase, OAuthRefreshUsecase
from src.application.account import AccountQuery
from src.domain.account import AccountRepository, AccountSecretRepository
from src.domain.credit import CreditRepository
from src.infrastructure.database.rdb import get_psql_session, TransactionClient
from src.infrastructure.email.resource import ResendEmailClient
from src.infrastructure.database.kvs.redis.session import RedisSessionClient
from src.infrastructure.oauth import JWTClient


def implement_oauth_signup_usecase(
        jwt: JWTClient = Depends(JWTClient()),
        session: Session = Depends(get_psql_session),
        account_repository: AccountRepository = Depends(implement_account_repository),
        account_secret_repository: AccountSecretRepository = Depends(implement_account_secret_repository),
        credit_repository: CreditRepository = Depends(implement_credit_repository)
    ) -> OAuthSignupUsecase:
    return OAuthSignupUsecase(
        jwt,
        ResendEmailClient(),
        TransactionClient(session),
        account_repository,
        account_secret_repository,
        credit_repository
    )


def implement_oauth_password_usecase(
        jwt: JWTClient = Depends(JWTClient()),
        account_query: AccountQuery = Depends(implement_account_query)
    ) -> OAuthPasswordUsecase:
    return OAuthPasswordUsecase(jwt, account_query)


def implement_oauth_refresh_usecase(
        jwt: JWTClient = Depends(JWTClient()),
        account_repository: AccountRepository = Depends(implement_account_repository)
    ) -> OAuthRefreshUsecase:
    return OAuthRefreshUsecase(jwt, account_repository)