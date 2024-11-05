import uuid
from typing import Optional
from datetime import datetime
from pydantic import Field
from pydantic import BaseModel


class CoreEntity(BaseModel):
    
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

    class ConfigDict:
        frozen = True
        from_attributes = True
        arbitrary_types_allowed = True
        validate_assignment = True


