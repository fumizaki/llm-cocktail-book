from fastapi import Depends, Header
from src.presentation.dependency.repository import (
    implement_account_repository,
)
from src.domain.entity.account import Account
from src.domain.entity.credential import Credential
from src.domain.repository.account import AccountRepository
from src.infrastructure.core.security.oauth import TokenClient, TokenPayload


def get_credential(
        authorization: str | None = Header(default=None),
        account_repository: AccountRepository = Depends(implement_account_repository),
    ) -> Credential:
    
    if authorization is None:
        raise Exception
    
    token = TokenClient.get_bearer_token(authorization)
    payload: TokenPayload = TokenClient.decode_token(token)

    account_in_db: Account = account_repository.get_exclude_deleted(payload.sub)
    return Credential(id=account_in_db.id, email=account_in_db.email)