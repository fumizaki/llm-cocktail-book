from fastapi import APIRouter, status, HTTPException, Depends, Request
from src.presentation.dependency.usecase.webhook import implement_stripe_webhook_usecase
from src.application.webhook import StripeWebhookUsecase


router = APIRouter()


@router.post("/stripe/webhook")
async def stripe_webhook(usecase: StripeWebhookUsecase = Depends(implement_stripe_webhook_usecase)):
    result = await usecase.process_exec()