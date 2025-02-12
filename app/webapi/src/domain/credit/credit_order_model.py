from ..model import Model

class CreateCreditOrderModel(Model):
    amount: int
    currency: str

class CreateCreditOrderResult(Model):
    amount: int
    currency: str
    client_secret: str