from pydantic import BaseModel

class StripePaymentIntentStatusResult(BaseModel):
    id: str
    client_secret: str
    status: str