from fastapi import Depends, Header, Query
from src.presentation.dependency.repository.account import (
    implement_account_repository,
)
from src.application.core import Credential
from src.domain.entity.account import Account
from src.domain.repository.account import AccountRepository
from src.infrastructure.oauth import JWTClient, Payload, parse_bearer_token


def get_credential_from_header(
        authorization: str | None = Header(default=None),
        jwt: JWTClient = Depends(JWTClient()),
        account_repository: AccountRepository = Depends(implement_account_repository),
    ) -> Credential:
    
    if authorization is None:
        raise Exception
    
    token = parse_bearer_token(authorization)
    payload: Payload = jwt.decode(token)

    account_in_db: Account = account_repository.get_exclude_deleted(payload.sub)
    return Credential(account_id=account_in_db.id, email=account_in_db.email)


def get_credential_from_query(
        header: str | None = Query(default=None),
        jwt: JWTClient = Depends(JWTClient()),
        account_repository: AccountRepository = Depends(implement_account_repository),
    ) -> Credential:

    if header is None:
        raise Exception
    
    payload: Payload = jwt.decode(header)

    account_in_db: Account = account_repository.get_exclude_deleted(payload.sub)
    return Credential(account_id=account_in_db.id, email=account_in_db.email)