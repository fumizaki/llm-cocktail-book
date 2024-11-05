from typing import Optional
from src.domain.schema.core import CoreSchema
from src.infrastructure.core.security.oauth import AuthGrantType, TokenType

class OAuthSignupRequestParams(CoreSchema):
    email: str
    password: str
    redirect_url: Optional[str] = None


class OAuthPasswordRequestParams(CoreSchema):
    grant_type: AuthGrantType
    email: str
    password: str
    scope: Optional[str] = None

class OAuthPasswordResponseParams(CoreSchema):
    access_token: str
    token_type: TokenType
    expires_in: int
    refresh_token: str
    scope: Optional[str] = None
    id_token: Optional[str] = None