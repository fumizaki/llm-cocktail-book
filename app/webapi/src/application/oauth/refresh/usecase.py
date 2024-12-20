from fastapi import HTTPException, status
from src.application.oauth.core import OAuthTokenModel
from src.application.oauth.refresh import OAuthRefreshModel
from src.domain.repository.account import AccountRepository
from src.infrastructure.core.security.jwt import JWTClient, TokenType, JWTPayload


class OAuthRefreshUsecase:

    def __init__(
        self,
        account_repository: AccountRepository,
    ) -> None:
        self.account_repository = account_repository


    def token_exec(self, params: OAuthRefreshModel) -> OAuthTokenModel:
        token_payload: JWTPayload = JWTClient.decode_token(params.refresh_token)
        account_in_db = self.account_repository.get_exclude_deleted(token_payload.sub)
        
        access_token_exp = JWTClient.get_expires_in(1)
        access_token = JWTClient.encode_token(
            member_id=account_in_db.id,
            expires_in=access_token_exp
        )
        refresh_token = JWTClient.encode_token(
            member_id=account_in_db.id,
            expires_in=JWTClient.get_expires_in(30)
        )
        
        return OAuthTokenModel(
            access_token=access_token,
            token_type=TokenType.BEARER,
            expires_in=access_token_exp,
            refresh_token=refresh_token,
            scope=None,
            id_token=None # TODO: IDトークンを作成して付与する
        )
        