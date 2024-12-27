from typing import Optional
from src.application.core import CoreModel
from src.infrastructure.oauth import TokenType


class OAuthTokenModel(CoreModel):
    access_token: str
    token_type: TokenType
    expires_in: int
    refresh_token: str
    scope: Optional[str] = None
    id_token: Optional[str] = None