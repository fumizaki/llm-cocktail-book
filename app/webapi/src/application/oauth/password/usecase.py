from fastapi import HTTPException, status
from src.application.oauth.core import OAuthTokenModel
from src.application.oauth.password import OAuthPasswordModel
from src.domain.query.account import AccountQuery
from src.infrastructure.hashing import HashingClient
from src.infrastructure.oauth import JWTClient, TokenType


class OAuthPasswordUsecase:

    def __init__(
        self,
        jwt: JWTClient,
        account_query: AccountQuery,
    ) -> None:
        self.jwt = jwt
        self.account_query = account_query


    def token_exec(self, params: OAuthPasswordModel) -> OAuthTokenModel:
        account_in_db = self.account_query.get_account_with_secret(params.email)
        
        hasher = HashingClient(account_in_db.secret.salt, account_in_db.secret.stretching)
        
        if not hasher.verify(
                account_in_db.secret.password,
                params.password
            ):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid Request')
        
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
        