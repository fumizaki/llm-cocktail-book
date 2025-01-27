from pydantic import BaseModel

class StripeCheckoutLineItem(BaseModel):
    amount: int
    title: str
    quantity: int

class StripeCheckoutSessionModel(BaseModel):
    currency: str
    line_items: list[StripeCheckoutLineItem]


class StripeCheckoutSessionResult(BaseModel):
    session_id: str
    checkout_url: str
    status: str


class StripePaymentIntentResult(BaseModel):
    client_secret: str