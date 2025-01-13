from fastapi import HTTPException, status
from src.application.oauth.core import OAuthTokenModel
from src.application.oauth.refresh import OAuthRefreshModel
from src.domain.repository.account import AccountRepository
from src.infrastructure.oauth import JWTClient, TokenType, AuthorizationTokenPayload


class OAuthRefreshUsecase:

    def __init__(
        self,
        jwt: JWTClient,
        account_repository: AccountRepository,
    ) -> None:
        self.jwt = jwt
        self.account_repository = account_repository


    def token_exec(self, params: OAuthRefreshModel) -> OAuthTokenModel:
        payload: AuthorizationTokenPayload = self.jwt.decode_authorization_token(params.refresh_token)
        account_in_db = self.account_repository.get_exclude_deleted(payload.sub)
        
        # トークン作成
        access_token = self.jwt.encode_authorization_token(
            member_id=account_in_db.id,
            expires_in=self.jwt.access_token_exp
        )
        refresh_token = self.jwt.encode_authorization_token(
            member_id=account_in_db.id,
            expires_in=self.jwt.refresh_token_exp
        )
        
        return OAuthTokenModel(
            access_token=access_token,
            token_type=TokenType.BEARER,
            expires_in=self.jwt.access_token_exp,
            refresh_token=refresh_token,
            scope=None,
            id_token=None # TODO: IDトークンを作成して付与する
        )
        