from fastapi import Depends, Request
from sqlalchemy.orm import Session
from src.presentation.dependency.repository.credit import implement_credit_repository, implement_credit_transaction_repository, implement_credit_order_repository
from src.application.webhook import StripeWebhookUsecase
from src.domain.credit import CreditRepository, CreditTransactionRepository, CreditOrderRepository
from src.infrastructure.database.rdb import get_psql_session, TransactionClient
from src.infrastructure.payment import StripeWebhookClient


async def implement_stripe_webhook_usecase(
        request: Request,
        session: Session = Depends(get_psql_session),
        credit_repository: CreditRepository = Depends(implement_credit_repository),
        credit_transaction_repository: CreditTransactionRepository = Depends(implement_credit_transaction_repository),
        credit_order_repository: CreditOrderRepository = Depends(implement_credit_order_repository),
    ):
    stripe_webhook_client = StripeWebhookClient()
    stripe_webhook = await stripe_webhook_client.handle_webhook(request)
    return StripeWebhookUsecase(
        stripe_webhook,
        TransactionClient(session),
        credit_repository,
        credit_transaction_repository,
        credit_order_repository
    )