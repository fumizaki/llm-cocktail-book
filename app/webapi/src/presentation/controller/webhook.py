from fastapi import APIRouter, status, HTTPException, Depends, Request
from src.infrastructure.payment.resource import StripeWebhookClient

router = APIRouter()


@router.post("/stripe/webhook")
async def stripe_webhook(request: Request):
    stripe_webhook = StripeWebhookClient()
    result = await stripe_webhook.handle_webhook(request)
    print(f"result: {result}")