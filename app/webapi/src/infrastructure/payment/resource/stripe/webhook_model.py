from pydantic import BaseModel

class StripeWebhook(BaseModel):
    id: str
    event: str

class StripePaymentIntentWebhook(StripeWebhook):
    client_secret: str
    status: str