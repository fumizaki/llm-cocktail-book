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
from src.infrastructure.core.security.hash import HashClient
from src.infrastructure.core.security.jwt import JWTClient, TokenType
from src.infrastructure.email import build_signup_request_content, EmailClient
from src.infrastructure.database.kvs.redis.session import RedisSessionClient

class OAuthSignupUsecase:

    def __init__(
        self,
        mailer: EmailClient,
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


    def request_exec(self, params: OAuthSignupModel) -> None:
        # TODO:アカウントがいるか確認(いたらエラー)
        try:
            salt = HashClient.create_salt()
            stretching = HashClient.create_stretching()
            hashed = HashClient.hash(params.password, salt, stretching)
            id = str(uuid4())

            # kvsに格納(30min)
            self.kvs.set(id, {'email': params.email, 'salt': salt, 'stretching': stretching, 'password': hashed})

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

        except:
            self.tx.rollback()
        
