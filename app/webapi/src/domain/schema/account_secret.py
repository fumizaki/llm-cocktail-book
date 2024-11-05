from pydantic import Field
from src.domain.schema.core import CoreSchema

class UpdateAccountSecretParams(CoreSchema):
    current_password: str = Field(..., description='')
    new_password: str = Field(..., description='')
