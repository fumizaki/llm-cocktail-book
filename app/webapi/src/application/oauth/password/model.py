from typing import Optional
from src.application.core import CoreModel
from src.infrastructure.oauth import GrantType

class OAuthPasswordModel(CoreModel):
    grant_type: GrantType
    email: str
    password: str
    scope: Optional[str] = None

