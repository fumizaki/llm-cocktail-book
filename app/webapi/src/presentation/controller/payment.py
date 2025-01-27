from fastapi import APIRouter, status, HTTPException, Depends
from src.presentation.dependency.usecase.payment import implement_payment_usecase
from src.application.payment import PaymentUsecase


router = APIRouter()


@router.post("/credit")
async def charge_credit(usecase: PaymentUsecase = Depends(implement_payment_usecase)):
    result = await usecase.checkout_exec()
    return result