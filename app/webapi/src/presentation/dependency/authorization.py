from fastapi import Depends, Header, Query
from src.presentation.dependency.repository import (
    implement_account_repository,
)
from src.domain.entity.account import Account
from src.domain.entity.credential import Credential
from src.domain.repository.account import AccountRepository
from src.infrastructure.core.security.jwt import JWTClient, JWTPayload


def get_credential_from_header(
        authorization: str | None = Header(default=None),
        account_repository: AccountRepository = Depends(implement_account_repository),
    ) -> Credential:
    
    if authorization is None:
        raise Exception
    
    token = JWTClient.get_bearer_token(authorization)
    payload: JWTPayload = JWTClient.decode_token(token)

    account_in_db: Account = account_repository.get_exclude_deleted(payload.sub)
    return Credential(id=account_in_db.id, email=account_in_db.email)


def get_credential_from_query(
        header: str | None = Query(default=None),
        account_repository: AccountRepository = Depends(implement_account_repository),
    ) -> Credential:

    if header is None:
        raise Exception
    
    payload: JWTPayload = JWTClient.decode_token(header)

    account_in_db: Account = account_repository.get_exclude_deleted(payload.sub)
    return Credential(id=account_in_db.id, email=account_in_db.email)