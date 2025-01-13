from __future__ import annotations
from typing import Optional
from datetime import datetime, timedelta
import jwt
from .model import (
    AuthorizationTokenPayload,
    VerificationTokenPayload
)
from .exception import (
    JWTException
)
from .params import (
    TOKEN_SECRET,
    ISSUER,
    AUDIENCE,
    ALGORITHM
)

class JWTClient:
    """JWT認証に関する操作を提供するクラス"""
    def __init__(self) -> None:
        self.iat: int = self.get_unixtime(days=0)
        self.verification_token_exp: int = self.get_unixtime(minutes=30)
        self.access_token_exp: int = self.get_unixtime(days=1)
        self.refresh_token_exp: int = self.get_unixtime(days=30)
        self.required_scopes: list[str] = []

    def __call__(self) -> JWTClient:
        return self
    
    def get_unixtime(self, *, days: int = 1, hours: int = 0, minutes: int = 0) -> int:
        """
        現在時刻からdaysで指定した日数を追加したunixtimeを取得

        Args:
            days (int): 追加する日数（デフォルト: 1）
            hours (int): 追加する時間数（デフォルト: 0）
            minutes (int): 追加する分数（デフォルト: 0）

        Returns:
            int: Unix timestamp
        """
        return int((datetime.now() + timedelta(days=days, hours=hours, minutes=minutes)).timestamp())


    def is_token_expired(self, exp: int) -> bool:
        """
        トークンが有効期限内かどうかを確認

        Args:
            exp (int): 有効期限のUnix timestamp

        Returns:
            bool: 有効期限内の場合はFalse
        """
        return exp < self.iat
    
    
    def is_valid_scopes(self, scopes: list[str]) -> bool:
        """
        必要なスコープが含まれているか確認

        Args:
            scopes (list[str]): 検証するスコープリスト

        Returns:
            bool: スコープが有効な場合はTrue
        """
        if len(self.required_scopes) == 0:
            return True
        return any(scope in scopes for scope in self.required_scopes)


    
    def encode_authorization_token(
        self,
        member_id: str,
        expires_in: int,
        scope: Optional[str] = None,
    ) -> str:
        """
        JWTトークンを生成

        Args:
            member_id (str): メンバーID
            expires_in (int): 有効期限
            scope (Optional[str]): スコープ

        Returns:
            str: 生成されたJWTトークン
        """
        payload = AuthorizationTokenPayload(
            sub=member_id,
            iss=ISSUER,
            aud=AUDIENCE,
            exp=expires_in,
            iat=self.iat,
            scope=scope
        )
        return jwt.encode(
            payload.model_dump(),
            TOKEN_SECRET,
            ALGORITHM
        )

    def decode_authorization_token(self, token: str) -> AuthorizationTokenPayload:
        try:
            payload = AuthorizationTokenPayload(**jwt.decode(
                token,
                TOKEN_SECRET,
                algorithms=[ALGORITHM],
                audience=AUDIENCE,
                issuer=ISSUER
            ))
            if self.is_token_expired(payload.exp):
                raise JWTException("Token has expired")
            return payload
        except jwt.InvalidSignatureError: # 具体的な例外をキャッチ
            raise JWTException("Invalid signature")
        except jwt.ExpiredSignatureError:
            raise JWTException("Token has expired")
        except jwt.InvalidAudienceError:
            raise JWTException("Invalid audience")
        except jwt.InvalidIssuerError:
            raise JWTException("Invalid issuer")
        except Exception as e: # 他の例外はまとめてキャッチ
            raise JWTException(f"Invalid token: {e}") # 元のエラーメッセージを含める


    def encode_verification_token(
        self,
        member_id: str,
        expires_in: int,
        redirect_url: Optional[str] = None,
        scope: Optional[str] = None,
    ) -> str:
        """
        JWTトークンを生成

        Args:
            member_id (str): メンバーID
            expires_in (int): 有効期限
            redirect_url (Optional[str]): リダイレクトURL
            scope (Optional[str]): スコープ

        Returns:
            str: 生成されたJWTトークン
        """
        payload = VerificationTokenPayload(
            sub=member_id,
            iss=ISSUER,
            aud=AUDIENCE,
            exp=expires_in,
            iat=self.iat,
            url=redirect_url,
            scope=scope
        )
        return jwt.encode(
            payload.model_dump(),
            TOKEN_SECRET,
            ALGORITHM
        )

    def decode_verification_token(
        self,
        token: str,
    ) -> VerificationTokenPayload:
        """
        JWTトークンをデコード

        Args:
            token (str): JWTトークン

        Returns:
            VerificationTokenPayload: デコードされたペイロード

        Raises:
            JWTException: トークンが無効な場合
        """
        try:
            payload = VerificationTokenPayload(**jwt.decode(
                token,
                TOKEN_SECRET,
                algorithms=[ALGORITHM],
                audience=AUDIENCE,
                issuer=ISSUER
            ))
            
            if self.is_token_expired(payload.exp):
                raise JWTException("Token has expired")
            
            return payload

        except jwt.InvalidSignatureError: # 具体的な例外をキャッチ
            raise JWTException("Invalid signature")
        except jwt.ExpiredSignatureError:
            raise JWTException("Token has expired")
        except jwt.InvalidAudienceError:
            raise JWTException("Invalid audience")
        except jwt.InvalidIssuerError:
            raise JWTException("Invalid issuer")
        except Exception as e: # 他の例外はまとめてキャッチ
            raise JWTException(f"Invalid token: {e}") # 元のエラーメッセージを含める
