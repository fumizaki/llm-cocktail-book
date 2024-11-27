from fastapi import HTTPException, status
from src.domain.query.account import AccountQuery
from src.domain.schema.oauth import OAuthPasswordRequestParams, OAuthPasswordResponseParams
from src.infrastructure.core.security.hash import HashClient
from src.infrastructure.core.security.jwt import JWTClient, TokenType


class OAuthPasswordUsecase:

    def __init__(
        self,
        account_query: AccountQuery,
    ) -> None:
        self.account_query = account_query


    def token_exec(self, params: OAuthPasswordRequestParams) -> OAuthPasswordResponseParams:
        account_in_db = self.account_query.get_account_with_secret(params.email)
        if not HashClient.verify(
                account_in_db.secret.password,
                params.password,
                account_in_db.secret.salt,
                account_in_db.secret.stretching
            ):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid Request')
        
        access_token_exp = JWTClient.get_expires_in(1)
        access_token = JWTClient.encode_token(
            member_id=account_in_db.id,
            expires_in=access_token_exp
        )
        refresh_token = JWTClient.encode_token(
            member_id=account_in_db.id,
            expires_in=JWTClient.get_expires_in(30)
        )
        
        return OAuthPasswordResponseParams(
            access_token=access_token,
            token_type=TokenType.BEARER,
            expires_in=access_token_exp,
            refresh_token=refresh_token,
            scope=None,
            id_token=None # TODO: IDトークンを作成して付与する
        )
        