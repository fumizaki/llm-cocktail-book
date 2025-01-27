from fastapi import HTTPException, status
from ..credential import Credential
from src.infrastructure.database.rdb import TransactionClient
from src.infrastructure.payment import StripePaymentClient, StripePaymentIntentResult
from src.infrastructure.logging import JsonLineLoggingClient


class PaymentUsecase:
    def __init__(
        self,
        credential: Credential,
        tx: TransactionClient,
    ) -> None:
        self.credential = credential
        self.tx = tx
        self.logger = JsonLineLoggingClient.get_logger(self.__class__.__name__)


    async def checkout_exec(self) -> StripePaymentIntentResult:
        payment = StripePaymentClient()
        return payment.create_payment_intent()