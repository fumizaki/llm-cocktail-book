from typing import Optional
from ..model import Model
from src.infrastructure.oauth import GrantType

class OAuthRefreshModel(Model):
    grant_type: GrantType
    refresh_token: str
    scope: Optional[str] = None

