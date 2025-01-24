from ..entity import Entity


class CreditTransaction(Entity):
    account_id: str
    transaction_type: str
    credit: int
    description: str


