from fastapi import Depends, Header, Query
from src.presentation.dependency.repository.account import (
    implement_account_repository,
)
from src.domain.account import AccountCredentialModel, Account, AccountRepository
from src.infrastructure.oauth import JWTClient, AuthorizationTokenPayload, parse_bearer_token


def get_credential_from_header(
        authorization: str | None = Header(default=None),
        jwt: JWTClient = Depends(JWTClient()),
        account_repository: AccountRepository = Depends(implement_account_repository),
    ) -> AccountCredentialModel:
    
    if authorization is None:
        raise Exception
    
    token = parse_bearer_token(authorization)
    payload: AuthorizationTokenPayload = jwt.decode_authorization_token(token)

    account_in_db: Account = account_repository.get_exclude_deleted(payload.sub)
    return AccountCredentialModel(account_id=account_in_db.id, email=account_in_db.email)


def get_credential_from_query(
        header: str | None = Query(default=None),
        jwt: JWTClient = Depends(JWTClient()),
        account_repository: AccountRepository = Depends(implement_account_repository),
    ) -> AccountCredentialModel:

    if header is None:
        raise Exception
    
    payload: AuthorizationTokenPayload = jwt.decode_authorization_token(header)

    account_in_db: Account = account_repository.get_exclude_deleted(payload.sub)
    return AccountCredentialModel(account_id=account_in_db.id, email=account_in_db.email)