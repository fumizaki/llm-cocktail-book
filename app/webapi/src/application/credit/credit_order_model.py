from ..model import Model

class CreateCreditOrderModel(Model):
    amount: int
    currency: str