from typing import Optional
from src.application.core import CoreModel
from src.infrastructure.core.security.jwt import AuthGrantType

class OAuthPasswordModel(CoreModel):
    grant_type: AuthGrantType
    email: str
    password: str
    scope: Optional[str] = None

