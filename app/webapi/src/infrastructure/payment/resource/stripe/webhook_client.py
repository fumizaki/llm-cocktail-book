from typing import Optional
from fastapi import Request, HTTPException
from .client import StripeClient
from .webhook_model import StripePaymentIntentStatusResult
import stripe

class StripeWebhookClient(StripeClient):
    def __init__(self) -> None:
        super().__init__()

    async def _handle_payment_intent_succeeded(self, payment_intent: stripe.PaymentIntent) -> StripePaymentIntentStatusResult:
        """payment_intent.succeededイベントの処理"""
        return StripePaymentIntentStatusResult(
                id=payment_intent.id,
                client_secret=payment_intent.client_secret,
                status='succeeded'
            )
    
    async def _handle_payment_intent_processing(self, payment_intent: stripe.PaymentIntent) -> StripePaymentIntentStatusResult:
        """payment_intent.processiongイベントの処理"""
        return StripePaymentIntentStatusResult(
                id=payment_intent.id,
                client_secret=payment_intent.client_secret,
                status='processing'
            )

    async def _handle_payment_intent_payment_failed(self, payment_intent: stripe.PaymentIntent) -> StripePaymentIntentStatusResult:
        """payment_intent.payment_failedイベントの処理"""
        return StripePaymentIntentStatusResult(
                id=payment_intent.id,
                client_secret=payment_intent.client_secret,
                status='failed'
            )

    async def handle_webhook(self, request: Request) -> StripePaymentIntentStatusResult | None:
        """Webhookリクエストを処理する"""
        try:
            payload = await request.body()
            sig_header = request.headers.get("stripe-signature")

            event: stripe.Event = stripe.Webhook.construct_event(
                payload, sig_header, self.endpoint_secret
            )
            
            if event.type == "payment_intent.succeeded":
                return await self._handle_payment_intent_succeeded(event.data.object)
            elif event.type == "payment_intent.processing":
                return await self._handle_payment_intent_processing(event.data.object)
            elif event.type == "payment_intent.payment_failed":
                return await self._handle_payment_intent_payment_failed(event.data.object)
            else:
                print(f"Skip processing event: {event.type}")

        except ValueError as e:
            # Invalid payload
            raise HTTPException(status_code=400, detail="Invalid payload")
        
'''
# URLs
# https://docs.stripe.com/webhooks
# https://docs.stripe.com/stripe-cli
# https://docs.stripe.com/stripe-cli/keys
'''