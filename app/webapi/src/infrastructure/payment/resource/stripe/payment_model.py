from pydantic import BaseModel

class CheckoutLineItem(BaseModel):
    amount: int
    title: str
    quantity: int

class CheckoutSessionModel(BaseModel):
    currency: str
    line_items: list[CheckoutLineItem]


class CheckoutSessionResult(BaseModel):
    session_id: str
    checkout_url: str
    status: str