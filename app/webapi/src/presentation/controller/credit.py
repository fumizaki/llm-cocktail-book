from fastapi import APIRouter, status, HTTPException, Depends
from src.presentation.dependency.usecase.credit import implement_credit_order_usecase
from src.application.credit import CreditOrderUsecase, CreateCreditOrderModel


router = APIRouter()


@router.post("/credit/order")
async def charge_credit(form: CreateCreditOrderModel, usecase: CreditOrderUsecase = Depends(implement_credit_order_usecase)):
    result = await usecase.checkout_exec(form)
    return result