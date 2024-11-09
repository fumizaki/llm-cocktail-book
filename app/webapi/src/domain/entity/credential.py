from pydantic import BaseModel


class Credential(BaseModel):
    id: str
    email: str
