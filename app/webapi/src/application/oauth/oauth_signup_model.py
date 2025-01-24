from typing import Optional
from ..model import Model

class OAuthSignupModel(Model):
    email: str
    password: str
    redirect_url: Optional[str] = "/"

