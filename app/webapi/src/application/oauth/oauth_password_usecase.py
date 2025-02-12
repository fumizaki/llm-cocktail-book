from fastapi import HTTPException, status
from src.application.account import AccountQuery
from src.domain.oauth import OAuthTokenModel, OAuthPasswordModel
from src.infrastructure.hashing import HashingClient
from src.infrastructure.oauth import JWTClient, TokenType
from src.infrastructure.logging import JsonLineLoggingClient

class OAuthPasswordUsecase:

    def __init__(
        self,
        jwt: JWTClient,
        account_query: AccountQuery,
    ) -> None:
        self.jwt = jwt
        self.account_query = account_query
        self.logger = JsonLineLoggingClient.get_logger(self.__class__.__name__)


    def token_exec(self, params: OAuthPasswordModel) -> OAuthTokenModel:
        self.logger.info(f"Token execution started for email: {params.email}")

        try:
            account_in_db = self.account_query.get_account_with_secret(params.email)
            self.logger.debug(f"Account retrieved: {account_in_db.id}")

            hasher = HashingClient(account_in_db.secret.salt, account_in_db.secret.stretching)
            
            if not hasher.verify(
                    account_in_db.secret.password,
                    params.password
                ):
                self.logger.warning(f"Invalid password attempt for email: {params.email}")
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid Request')
            
            self.logger.info(f"Password verified for account: {account_in_db.id}")

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
        