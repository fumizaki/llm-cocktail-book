from datetime import datetime
from fastapi import HTTPException, status
from uuid import uuid4
from src.domain.repository.account import AccountRepository
from src.domain.repository.account_secret import AccountSecretRepository
from src.domain.entity.account import Account
from src.domain.entity.account_secret import AccountSecret
from src.domain.schema.oauth import OAuthSignupRequestParams, OAuthPasswordResponseParams
from src.infrastructure.core.rdb.transaction import TransactionClient
from src.infrastructure.core.security.hash import HashClient
from src.infrastructure.core.security.oauth import TokenClient, TokenType
from src.infrastructure.core.email.content import build_signup_request_content
from src.infrastructure.resend.email import ResendEmailClient
from src.infrastructure.redis.session import RedisSessionClient

class OAuthSignupUsecase:

    def __init__(
        self,
        mailer: ResendEmailClient,
        kvs: RedisSessionClient,
        tx: TransactionClient,
        account_repository: AccountRepository,
        account_secret_repository: AccountSecretRepository,
    ) -> None:
        self.mailer = mailer
        self.kvs = kvs
        self.tx = tx
        self.account_repository = account_repository
        self.account_secret_repository = account_secret_repository


    def request_exec(self, params: OAuthSignupRequestParams) -> None:
        # TODO:アカウントがいるか確認(いたらエラー)
        try:
            salt = HashClient.create_salt()
            stretching = HashClient.create_stretching()
            hashed = HashClient.hash(params.password, salt, stretching)
            id = str(uuid4())

            # kvsに格納(30min)
            self.kvs.set(id, {'email': params.email, 'salt': salt, 'stretching': stretching, 'password': hashed})

            # メール送信
            content = build_signup_request_content(id)
            self.mailer.send_mail(
                to_add=[params.email],
                subject=content.subject,
                message=content.message
            )
            
            return
        
        except Exception as e:
            self.tx.rollback()


    def verify_exec(self, key: str) -> OAuthPasswordResponseParams:
        try:
            # kvsからデータを取得
            data = self.kvs.get(key)

            # アカウント作成
            account_in_db = self.account_repository.create(Account(email=data['email'], email_verified=datetime.now()))
            
            # シークレット作成
            self.account_secret_repository.create(
                AccountSecret(
                    account_id=account_in_db.id,
                    password=data['password'],
                    salt=data['salt'],
                    stretching=data['stretching']
                )
            )
            self.tx.commit()

            # トークン作成
            access_token_exp = TokenClient.get_expires_in(1)
            access_token = TokenClient.encode_token(
                member_id=account_in_db.id,
                expires_in=access_token_exp
            )
            refresh_token = TokenClient.encode_token(
                member_id=account_in_db.id,
                expires_in=TokenClient.get_expires_in(30)
            )
            
            return OAuthPasswordResponseParams(
                access_token=access_token,
                token_type=TokenType.BEARER,
                expires_in=access_token_exp,
                refresh_token=refresh_token,
                scope=None,
                id_token=None # TODO: IDトークンを作成して付与する
            )

        except:
            self.tx.rollback()
        
