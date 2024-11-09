from fastapi import HTTPException, status
from src.domain.repository.account import AccountRepository
from src.domain.schema.oauth import OAuthRefreshRequestParams, OAuthRefreshResponseParams
from src.infrastructure.core.security.oauth import TokenClient, TokenType, TokenPayload


class OAuthRefreshUsecase:

    def __init__(
        self,
        account_repository: AccountRepository,
    ) -> None:
        self.account_repository = account_repository


    def token_exec(self, params: OAuthRefreshRequestParams) -> OAuthRefreshResponseParams:
        token_payload: TokenPayload = TokenClient.decode_token(params.refresh_token)
        account_in_db = self.account_repository.get_exclude_deleted(token_payload.sub)
        
        access_token_exp = TokenClient.get_expires_in(1)
        access_token = TokenClient.encode_token(
            member_id=account_in_db.id,
            expires_in=access_token_exp
        )
        refresh_token = TokenClient.encode_token(
            member_id=account_in_db.id,
            expires_in=TokenClient.get_expires_in(30)
        )
        
        return OAuthRefreshResponseParams(
            access_token=access_token,
            token_type=TokenType.BEARER,
            expires_in=access_token_exp,
            refresh_token=refresh_token,
            scope=None,
            id_token=None # TODO: IDトークンを作成して付与する
        )
        