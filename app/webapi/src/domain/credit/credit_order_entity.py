from ..entity import Entity


class CreditOrder(Entity):
    account_id: str
    provider: str
    reference_id: str
    credit: int
    amount: int
    currency: str
    status: str


