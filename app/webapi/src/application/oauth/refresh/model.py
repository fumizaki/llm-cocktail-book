from typing import Optional
from src.application.core import CoreModel
from src.infrastructure.oauth import GrantType

class OAuthRefreshModel(CoreModel):
    grant_type: GrantType
    refresh_token: str
    scope: Optional[str] = None

