from fastapi import APIRouter, status, HTTPException, Depends, Request
from src.presentation.dependency.usecase.credit import implement_credit_usecase, implement_credit_transaction_usecase, implement_credit_order_usecase
from src.application.credit import CreditUsecase, CreditTransactionUsecase, CreditOrderUsecase
from src.domain.credit import CreateCreditOrderModel


router = APIRouter()



@router.get("/credit")
async def get_credit(usecase: CreditUsecase = Depends(implement_credit_usecase)):
    result = await usecase.get_exec()
    return result


@router.get("/credit/transaction")
async def get_all_credit_transaction(usecase: CreditTransactionUsecase = Depends(implement_credit_transaction_usecase)):
    result = await usecase.get_all_exec()
    return result


@router.post("/credit/order")
async def order_credit(form: CreateCreditOrderModel, usecase: CreditOrderUsecase = Depends(implement_credit_order_usecase)):
    result = await usecase.checkout_exec(form)
    return result
