from datetime import datetime
from uuid import uuid4
from fastapi import HTTPException, status
from src.application.oauth.signup import OAuthSignupModel
from src.domain.repository.account import AccountRepository
from src.domain.repository.account_secret import AccountSecretRepository
from src.domain.entity.account import Account
from src.domain.entity.account_secret import AccountSecret
from src.infrastructure.database.rdb.transaction import TransactionClient
from src.infrastructure.hashing import HashingClient
from src.infrastructure.oauth import JWTClient
from src.infrastructure.email import build_signup_request_content, EmailClient
from src.infrastructure.database.kvs.redis.session import RedisSessionClient

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


    def request_exec(self, params: OAuthSignupModel) -> None:
        
        try:
            account_in_db: Account = self.account_repository.create(Account(
                email=params.email
            ))
            hasher = HashingClient()
            hashed = hasher.hash(params.password)

            self.account_secret_repository.create(AccountSecret(
                account_id=account_in_db.id,
                password=hashed,
                salt=hasher.salt,
                stretching=hasher.stretching
            ))

            # TODO: 有効期限を設定したトークンを作成し、メールのcontentに入れる
            verification_token = self.jwt.encode_verification(
                account_in_db.id,
                self.jwt.verification_token_exp,
                params.redirect_url
            )

            # メール送信
            self.mailer.send_mail(
                to_add=[params.email],
                content=build_signup_request_content(verification_token)
            )
            
            return
        
        except Exception as e:
            self.tx.rollback()


    def verify_exec(self, key: str) -> str:
        try:
            verification_payload = self.jwt.decode_verification(key)

            account_in_db: Account = self.account_repository.get_exclude_deleted(verification_payload.sub)
            self.account_repository.verify(account_in_db.id, datetime.now())
            self.tx.commit()
            return verification_payload.url

        except:
            self.tx.rollback()
        
