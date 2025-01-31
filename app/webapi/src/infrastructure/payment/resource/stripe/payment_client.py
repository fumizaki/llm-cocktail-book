from typing import Optional
from .client import StripeClient
from .payment_model import StripePaymentIntentModel, StripePaymentIntentResult
from .payment_exception import StripePaymentError

class StripePaymentClient(StripeClient):
    def __init__(self) -> None:
        super().__init__()

    def create_payment_intent(self, params: StripePaymentIntentModel) -> StripePaymentIntentResult:
        try:
            payment_intent = self.client.payment_intents.create({
                'amount': params.amount,
                'currency': params.currency,
                'automatic_payment_methods': {"enabled": True},
            })

            if payment_intent.client_secret is None:
                raise

            return StripePaymentIntentResult(
                id=payment_intent.id,
                amount=params.amount,
                currency=params.currency,
                client_secret=payment_intent.client_secret
            )

        except Exception as e:
            raise StripePaymentError(f"Invalid response from Stripe API: {e}")


'''
# URLs
# https://docs.stripe.com/payments/quickstart
# https://docs.stripe.com/payments/accept-a-payment?=&ui=elements
'''