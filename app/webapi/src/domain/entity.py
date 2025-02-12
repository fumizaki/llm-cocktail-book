import uuid
from typing import Optional
from datetime import datetime
from pydantic import Field
from .model import Model


class Entity(Model):
    
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None



