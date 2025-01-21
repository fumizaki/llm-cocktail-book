from datetime import datetime
from fastapi import HTTPException, status
from .oauth_signup_model import OAuthSignupModel
from src.domain.account import Account, AccountRepository, AccountSecretRepository, AccountSecret
from src.infrastructure.database.rdb.transaction import TransactionClient
from src.infrastructure.hashing import HashingClient
from src.infrastructure.oauth import JWTClient
from src.infrastructure.email import build_signup_request_content, EmailClient
from src.infrastructure.logging import JsonLineLoggingClient


class OAuthSignupUsecase:

    def __init__(
        self,
        jwt: JWTClient,
        mailer: EmailClient,
        tx: TransactionClient,
        account_repository: AccountRepository,
        account_secret_repository: AccountSecretRepository,
    ) -> None:
        self.jwt = jwt
        self.mailer = mailer
        self.tx = tx
        self.account_repository = account_repository
        self.account_secret_repository = account_secret_repository
        self.logger = JsonLineLoggingClient.get_logger(self.__class__.__name__)


    def request_exec(self, params: OAuthSignupModel) -> None:
        self.logger.info(f"Reequest execution started for email: {params.email}")
        
        try:
            self.logger.info(f"Create Account with unverified email: {params.email}")
            account_in_db: Account = self.account_repository.create(Account(
                email=params.email
            ))
            hasher = HashingClient()
            hashed = hasher.hash(params.password)

            self.logger.info(f"Account Secret created for account: {account_in_db.id}")
            self.account_secret_repository.create(AccountSecret(
                account_id=account_in_db.id,
                password=hashed,
                salt=hasher.salt,
                stretching=hasher.stretching
            ))

            self.logger.debug(f"Verification Token generated for account: {account_in_db.id}")
            verification_token = self.jwt.encode_verification_token(
                account_in_db.id,
                self.jwt.verification_token_exp,
                params.redirect_url
            )

            # メール送信
            self.logger.info(f"Sending Email for account verification: {account_in_db.email}")
            self.mailer.send_mail(
                to_add=[params.email],
                content=build_signup_request_content(verification_token)
            )

            self.tx.commit()

        
        except HTTPException as http_exc:
            self.logger.error(f"HTTPException occurred: {http_exc.detail}")
            self.tx.rollback()
            raise

        except Exception as exc:
            self.logger.critical(f"Unexpected error during token execution: {str(exc)}", exc_info=True)
            self.tx.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail='Internal Server Error'
            )

            


    def verify_exec(self, key: str) -> str:
        self.logger.info(f"Verify execution started for : xxx")
        try:
            payload = self.jwt.decode_verification_token(key)

            self.logger.debug(f"Verify Account: {payload.sub}")
            account_in_db: Account = self.account_repository.get_exclude_deleted(payload.sub)
            
            
            self.account_repository.verify(account_in_db.id, datetime.now())
            self.tx.commit()

            return payload.url

        except HTTPException as http_exc:
            self.logger.error(f"HTTPException occurred: {http_exc.detail}")
            self.tx.rollback()
            raise

        except Exception as exc:
            self.logger.critical(f"Unexpected error during token execution: {str(exc)}", exc_info=True)
            self.tx.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail='Internal Server Error'
            )
        
