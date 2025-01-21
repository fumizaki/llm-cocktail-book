from typing import Optional
from datetime import datetime
from ..entity import Entity


class Account(Entity):
    email: str
    email_verified: Optional[datetime] = None

