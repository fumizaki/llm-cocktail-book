from typing import Optional
from ..model import Model
from src.infrastructure.oauth import GrantType

class OAuthPasswordModel(Model):
    grant_type: GrantType
    email: str
    password: str
    scope: Optional[str] = None

