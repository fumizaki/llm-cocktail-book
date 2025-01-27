from typing import Optional
from .client import StripeClient
from .payment_model import StripePaymentIntentResult
from .payment_exception import StripePaymentError

class StripePaymentClient(StripeClient):
    def __init__(self, api_key: Optional[str] = None) -> None:
        super().__init__(api_key)

    def create_payment_intent(self) -> StripePaymentIntentResult:
        try:
            intent = self.client.payment_intents.create({
                'amount': 1099,
                'currency': "jpy",
                'automatic_payment_methods': {"enabled": True},
            })
            return StripePaymentIntentResult(
                client_secret=intent.client_secret
            )

        except Exception as e:
            raise StripePaymentError(f"Invalid response from Stripe API: {e}")
        

    # def create_checkout_session(self, params: StripeCheckoutSessionModel) -> StripeCheckoutSessionResult:
    #     try:
    #         session = self.client.checkout.sessions.create(
    #             payment_method_types=['card'],
    #             mode='payment',
    #             line_items = [{
    #                 'price_data': {
    #                     'currency': params.currency,
    #                     'unit_amount': item.amount,
    #                     'product_data': {
    #                         'name': item.title
    #                     }
    #                 },
    #                 'quantity': item.quantity
    #             } for item in params.line_items]
    #         )
    #         return StripeCheckoutSessionResult(
    #             session_id=session.id,
    #             checkout_url=session.url,
    #             status=session.status,
    #         )
    #     except Exception as e:
    #         raise StripePaymentError(f"Invalid response from Stripe API: {e}")
