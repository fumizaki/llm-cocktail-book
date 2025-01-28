from pydantic import BaseModel

class StripePaymentIntentModel(BaseModel):
    amount: int
    currency: str

class StripePaymentIntentResult(BaseModel):
    id: str
    amount: int
    currency: str
    client_secret: str