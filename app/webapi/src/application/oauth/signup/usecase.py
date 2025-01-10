from datetime import datetime
from uuid import uuid4
from fastapi import HTTPException, status
from src.application.oauth.core import OAuthTokenModel
from src.application.oauth.signup import OAuthSignupModel
from src.domain.repository.account import AccountRepository
from src.domain.repository.account_secret import AccountSecretRepository
from src.domain.entity.account import Account
from src.domain.entity.account_secret import AccountSecret
from src.infrastructure.database.rdb.transaction import TransactionClient
from src.infrastructure.hashing import HashingClient
from src.infrastructure.oauth import JWTClient, TokenType
from src.infrastructure.email import build_signup_request_content, EmailClient
from src.infrastructure.database.kvs.redis.session import RedisSessionClient

class OAuthSignupUsecase:

    def __init__(
        self,
        jwt: JWTClient,
        mailer: EmailClient,
        kvs: RedisSessionClient,
        tx: TransactionClient,
        account_repository: AccountRepository,
        account_secret_repository: AccountSecretRepository,
    ) -> None:
        self.jwt = jwt
        self.mailer = mailer
        self.kvs = kvs
        self.tx = tx
        self.account_repository = account_repository
        self.account_secret_repository = account_secret_repository


    def request_exec(self, params: OAuthSignupModel) -> None:
        # TODO:アカウントがいるか確認(いたらエラー)
        try:
            
            hasher = HashingClient()
            hashed = hasher.hash(params.password)
            id = str(uuid4())

            # kvsに格納(30min)
            self.kvs.set(id, {'email': params.email, 'salt': hasher.salt, 'stretching': hasher.stretching, 'password': hashed})

            # メール送信
            self.mailer.send_mail(
                to_add=[params.email],
                content=build_signup_request_content(id)
            )
            
            return
        
        except Exception as e:
            self.tx.rollback()


    def verify_exec(self, key: str) -> OAuthTokenModel:
        try:
            # kvsからデータを取得
            data = self.kvs.get(key)
            # TODO: validation

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
            access_token = self.jwt.encode(
                member_id=account_in_db.id,
                expires_in=self.jwt.access_token_exp
            )
            refresh_token = self.jwt.encode(
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

        except:
            self.tx.rollback()
        
