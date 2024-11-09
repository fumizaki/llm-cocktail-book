import os
from typing import Optional
from enum import Enum
from datetime import datetime, timedelta
from dotenv import load_dotenv
import jwt
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer

load_dotenv()

OAUTH2_ISSUER: str = os.getenv('OAUTH2_ISSUER', '')
OAUTH2_AUDIENCE: str = os.getenv('OAUTH2_AUDIENCE', '')
OAUTH2_ALGORITHM: str = os.getenv('OAUTH2_ALGORITHM', '')
OAUTH2_TOKEN_SECRET: str = os.getenv('OAUTH2_TOKEN_SECRET', '')
OAUTH2_CODE_SECRET: str = os.getenv('OAUTH2_CODE_SECRET', '')


class AuthResponseType(str, Enum):
    CODE = 'code'
    TOKEN = 'token'
    ID_TOKEN = 'id_token'


class TokenType(str, Enum):
    BEARER = 'Bearer'
    MAC = 'MAC'
    JWT = 'JWT'
    
    
class AuthGrantType(str, Enum):
    AUTHORIZATION_CODE = 'authorization_code'
    PASSWORD = 'password'
    CLIENT_CREDENTIALS = 'client_credentials'
    REFRESH_TOKEN = 'refresh_token'
    

class TokenPayload(BaseModel):
    # メンバーID
    sub: str
    # 発行者
    iss: str
    # 対象者
    aud: str
    # 有効期限
    exp: int
    # 発行日時
    iat: int
    # スコープ
    scope: Optional[str] = None
    # JWTのID
    jti: Optional[str] = None
    # ノンス
    nonce: Optional[str] = None



class TokenClient:

    def get_expires_in(days: int = 1) -> int:
        """
        現在時刻からdaysで指定した日数を追加したunixtime
        """
        return int((datetime.now() + timedelta(days)).timestamp())


    def get_iat() -> int:
        return TokenClient.get_expires_in(0)


    def is_scope_inclueded(scope: str, scopes: list[str]) -> bool:
        return scope in scopes


    def is_effective(expires_in: int) -> bool:
        return expires_in > int(datetime.now().timestamp())


    def encode_token(
        member_id: str,
        expires_in: int,
        scope: Optional[str] = None,
        secret: str = OAUTH2_TOKEN_SECRET
        ) -> str:

        payload = TokenPayload(
            sub=member_id,
            iss=OAUTH2_ISSUER,
            aud=OAUTH2_AUDIENCE,
            exp=expires_in,
            iat=TokenClient.get_iat(),
            scope=scope
        )
        return jwt.encode(payload.model_dump(), secret, OAUTH2_ALGORITHM)


    def decode_token(token: str, secret: str = OAUTH2_TOKEN_SECRET) -> TokenPayload:
        try:
            payload: TokenPayload = TokenPayload(**jwt.decode(
                token,
                secret,
                algorithms=[OAUTH2_ALGORITHM],
                audience=OAUTH2_AUDIENCE,
                issuer=OAUTH2_ISSUER
                )
            )
            if not TokenClient.is_effective(payload.exp):
                raise jwt.exceptions.InvalidTokenError
            
            return payload

        except Exception:
            raise jwt.exceptions.InvalidTokenError


    def get_bearer_token(authorization: str) -> str:
        scheme, _, param = authorization.partition(" ")
        if scheme.lower() != "bearer":
            raise Exception
        return param


    def is_valid_scope(required_scopes: list[str], scopes: list[str]) -> bool:
        if len(required_scopes) == 0:
            return True

        is_valid = False
        for scope in required_scopes:
            if scope in scopes:
                is_valid = True
                break

        return is_valid