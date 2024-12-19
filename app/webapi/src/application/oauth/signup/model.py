from typing import Optional
from src.application.core import CoreModel

class OAuthSignupModel(CoreModel):
    email: str
    password: str
    redirect_url: Optional[str] = None

