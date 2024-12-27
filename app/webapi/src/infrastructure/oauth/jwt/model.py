from typing import Optional
from enum import Enum
from pydantic import BaseModel

class AuthenticationResponseType(str, Enum):
    """認証レスポンスタイプ"""
    CODE = 'code'
    TOKEN = 'token'
    ID_TOKEN = 'id_token'


class TokenType(str, Enum):
    """トークンタイプ"""
    BEARER = 'Bearer'
    MAC = 'MAC'
    JWT = 'JWT'


class GrantType(str, Enum):
    """認可グラントタイプ"""
    AUTHORIZATION_CODE = 'authorization_code'
    PASSWORD = 'password'
    CLIENT_CREDENTIALS = 'client_credentials'
    REFRESH_TOKEN = 'refresh_token'


class Payload(BaseModel):
    sub: str
    iss: str
    aud: str
    exp: int
    iat: int
    scope: Optional[str] = None
    jti: Optional[str] = None
    nonce: Optional[str] = None