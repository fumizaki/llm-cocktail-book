import os
from typing import Optional
from enum import Enum
from datetime import datetime, timedelta
from dotenv import load_dotenv
import jwt
from pydantic import BaseModel, Field
from jwt.exceptions import InvalidTokenError

load_dotenv()


class OAuth2Config:
    """OAuth2の設定値を管理するクラス"""
    ISSUER: str = os.getenv('OAUTH2_ISSUER', '')
    AUDIENCE: str = os.getenv('OAUTH2_AUDIENCE', '')
    ALGORITHM: str = os.getenv('OAUTH2_ALGORITHM', '')
    TOKEN_SECRET: str = os.getenv('OAUTH2_TOKEN_SECRET', '')


class AuthResponseType(str, Enum):
    """認証レスポンスタイプ"""
    CODE = 'code'
    TOKEN = 'token'
    ID_TOKEN = 'id_token'


class TokenType(str, Enum):
    """トークンタイプ"""
    BEARER = 'Bearer'
    MAC = 'MAC'
    JWT = 'JWT'


class AuthGrantType(str, Enum):
    """認可グラントタイプ"""
    AUTHORIZATION_CODE = 'authorization_code'
    PASSWORD = 'password'
    CLIENT_CREDENTIALS = 'client_credentials'
    REFRESH_TOKEN = 'refresh_token'


class JWTPayload(BaseModel):
    """JWTペイロードのデータモデル"""
    sub: str = Field(..., description="メンバーID")
    iss: str = Field(..., description="発行者")
    aud: str = Field(..., description="対象者")
    exp: int = Field(..., description="有効期限")
    iat: int = Field(..., description="発行日時")
    scope: Optional[str] = Field(None, description="スコープ")
    jti: Optional[str] = Field(None, description="JWTのID")
    nonce: Optional[str] = Field(None, description="ノンス")


class JWTException(Exception):
    """JWT関連の例外クラス"""
    pass


class InvalidBearerTokenError(JWTException):
    """不正なBearer tokenの例外"""
    pass


class JWTClient:
    """JWT認証に関する操作を提供するクラス"""

    @staticmethod
    def get_expires_in(days: int = 1) -> int:
        """
        現在時刻からdaysで指定した日数を追加したunixtimeを取得

        Args:
            days (int): 追加する日数（デフォルト: 1）

        Returns:
            int: Unix timestamp
        """
        return int((datetime.now() + timedelta(days=days)).timestamp())

    @staticmethod
    def get_iat() -> int:
        """
        現在のunixtimeを取得

        Returns:
            int: 現在のUnix timestamp
        """
        return int(datetime.now().timestamp())

    @staticmethod
    def is_scope_included(scope: str, scopes: list[str]) -> bool:
        """
        指定されたスコープがスコープリストに含まれているか確認

        Args:
            scope (str): 確認するスコープ
            scopes (list[str]): スコープリスト

        Returns:
            bool: 含まれている場合はTrue
        """
        return scope in scopes

    @staticmethod
    def is_effective(expires_in: int) -> bool:
        """
        トークンが有効期限内かどうかを確認

        Args:
            expires_in (int): 有効期限のUnix timestamp

        Returns:
            bool: 有効期限内の場合はTrue
        """
        return expires_in > int(datetime.now().timestamp())

    @classmethod
    def encode_token(
        cls,
        member_id: str,
        expires_in: int,
        scope: Optional[str] = None,
        secret: str = OAuth2Config.TOKEN_SECRET
    ) -> str:
        """
        JWTトークンを生成

        Args:
            member_id (str): メンバーID
            expires_in (int): 有効期限
            scope (Optional[str]): スコープ
            secret (str): 秘密鍵

        Returns:
            str: 生成されたJWTトークン
        """
        payload = JWTPayload(
            sub=member_id,
            iss=OAuth2Config.ISSUER,
            aud=OAuth2Config.AUDIENCE,
            exp=expires_in,
            iat=cls.get_iat(),
            scope=scope
        )
        return jwt.encode(
            payload.model_dump(),
            secret,
            OAuth2Config.ALGORITHM
        )

    @classmethod
    def decode_token(
        cls,
        token: str,
        secret: str = OAuth2Config.TOKEN_SECRET
    ) -> JWTPayload:
        """
        JWTトークンをデコード

        Args:
            token (str): JWTトークン
            secret (str): 秘密鍵

        Returns:
            JWTPayload: デコードされたペイロード

        Raises:
            InvalidTokenError: トークンが無効な場合
        """
        try:
            payload = JWTPayload(**jwt.decode(
                token,
                secret,
                algorithms=[OAuth2Config.ALGORITHM],
                audience=OAuth2Config.AUDIENCE,
                issuer=OAuth2Config.ISSUER
            ))
            
            if not cls.is_effective(payload.exp):
                raise InvalidTokenError("Token has expired")
            
            return payload

        except Exception as e:
            raise InvalidTokenError(str(e))

    @staticmethod
    def get_bearer_token(authorization: str) -> str:
        """
        Authorization headerからBearer tokenを抽出

        Args:
            authorization (str): Authorization header値

        Returns:
            str: Bearer token

        Raises:
            InvalidBearerTokenError: Bearer tokenが不正な場合
        """
        scheme, _, param = authorization.partition(" ")
        if scheme.lower() != "bearer":
            raise InvalidBearerTokenError("Invalid authorization scheme")
        if not param:
            raise InvalidBearerTokenError("Token is missing")
        return param

    @staticmethod
    def is_valid_scope(required_scopes: list[str], scopes: list[str]) -> bool:
        """
        必要なスコープが含まれているか確認

        Args:
            required_scopes (list[str]): 必要なスコープリスト
            scopes (list[str]): 持っているスコープリスト

        Returns:
            bool: スコープが有効な場合はTrue
        """
        if not required_scopes:
            return True
        return any(scope in scopes for scope in required_scopes)