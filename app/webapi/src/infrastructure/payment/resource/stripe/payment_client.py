from .client import StripeClient
from .payment_model import CheckoutSessionModel, CheckoutSessionResult
from .payment_exception import StripePaymentError

class StripePaymentClient(StripeClient):
    def __init__(self, api_key: str | None = None) -> None:
        super().__init__(api_key)

    def create_checkout_session(self, params: CheckoutSessionModel) -> CheckoutSessionResult:
        try:
            session = self.client.checkout.sessions.create(
                payment_method_types=['card'],
                mode='payment',
                line_items = [{
                    'price_data': {
                        'currency': params.currency,
                        'unit_amount': item.amount,
                        'product_data': {
                            'name': item.title
                        }
                    },
                    'quantity': item.quantity
                } for item in params.line_items]
            )
            return CheckoutSessionResult(
                session_id=session.id,
                checkout_url=session.url,
                status=session.status,
            )
        except Exception as e:
            raise StripePaymentError(f"Invalid response from Stripe API: {e}")
