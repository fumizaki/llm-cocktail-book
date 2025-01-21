from typing import Optional
from ..model import Model
from src.infrastructure.oauth import TokenType


class OAuthTokenModel(Model):
    access_token: str
    token_type: TokenType
    expires_in: int
    refresh_token: str
    scope: Optional[str] = None
    id_token: Optional[str] = None