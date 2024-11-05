from typing import Optional
from datetime import datetime
from src.domain.entity.core import CoreEntity


class Account(CoreEntity):
    email: str
    email_verified: Optional[datetime] = None

