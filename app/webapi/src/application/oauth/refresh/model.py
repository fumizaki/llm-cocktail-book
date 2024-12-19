from typing import Optional
from src.application.core import CoreModel
from src.infrastructure.core.security.jwt import AuthGrantType

class OAuthRefreshModel(CoreModel):
    grant_type: AuthGrantType
    refresh_token: str
    scope: Optional[str] = None

