from fastapi import HTTPException, status
from .model import OAuthTokenModel
from .oauth_refresh_model import OAuthRefreshModel
from src.domain.account import AccountRepository
from src.infrastructure.oauth import JWTClient, TokenType, AuthorizationTokenPayload
from src.infrastructure.logging import JsonLineLoggingClient

class OAuthRefreshUsecase:

    def __init__(
        self,
        jwt: JWTClient,
        account_repository: AccountRepository,
    ) -> None:
        self.jwt = jwt
        self.account_repository = account_repository
        self.logger = JsonLineLoggingClient.get_logger(self.__class__.__name__)


    def token_exec(self, params: OAuthRefreshModel) -> OAuthTokenModel:
        self.logger.info(f"Token refresh execution started")

        try:
            
            payload: AuthorizationTokenPayload = self.jwt.decode_authorization_token(params.refresh_token)
            self.logger.info(f"Refresh Token decoded for account: {payload.sub} ")
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
            
            self.logger.info(f"Tokens generated for account: {account_in_db.id}")

            return OAuthTokenModel(
                access_token=access_token,
                token_type=TokenType.BEARER,
                expires_in=self.jwt.access_token_exp,
                refresh_token=refresh_token,
                scope=None,
                id_token=None # TODO: IDトークンを作成して付与する
            )
        except HTTPException as http_exc:
            self.logger.error(f"HTTPException occurred: {http_exc.detail}")
            raise

        except Exception as exc:
            self.logger.critical(f"Unexpected error during token execution: {str(exc)}", exc_info=True)
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail='Internal Server Error'
            )