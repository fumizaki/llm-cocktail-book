from fastapi import HTTPException, status
from ..credential import Credential
from .credit_order_model import CreateCreditOrderModel, CreateCreditOrderResult
from src.domain.credit import CreditOrder, CreditOrderRepository
from src.infrastructure.database.rdb import TransactionClient
from src.infrastructure.payment import StripePaymentClient, StripePaymentIntentModel
from src.infrastructure.logging import JsonLineLoggingClient

class CreditOrderUsecase:
    def __init__(
        self,
        credential: Credential,
        tx: TransactionClient,
        credit_order_repository: CreditOrderRepository,
    ) -> None:
        self.credential = credential
        self.tx = tx
        self.credit_order_repository = credit_order_repository
        self.payment = StripePaymentClient()
        self.logger = JsonLineLoggingClient.get_logger(self.__class__.__name__)


    async def checkout_exec(self, params: CreateCreditOrderModel) -> CreateCreditOrderResult:
        
        self.logger.info(f"Checkout Credit order execution started for account: {self.credential.account_id}")
        try:
            result = self.payment.create_payment_intent(
                StripePaymentIntentModel(
                    amount=params.amount,
                    currency=params.currency
                )
            )
            
            # TODO: currencyで算出方法を変更する必要がある
            credit = params.amount
            credit_order_in_db: CreditOrder = self.credit_order_repository.create(
                CreditOrder(
                    account_id=self.credential.account_id,
                    provider='stripe',
                    reference_id=result.id,
                    credit=credit,
                    amount=result.amount,
                    currency=result.currency,
                    status='pending'
                ))
            self.logger.info(f"Create Credit Order: {credit_order_in_db.id}")
            self.tx.commit()
            
            return CreateCreditOrderResult(
                amount=result.amount,
                currency=result.currency,
                client_secret=result.client_secret
            )
        
        except HTTPException as http_exc:
            self.logger.error(f"HTTPException occurred: {http_exc.detail}")
            self.tx.rollback()
            raise

        except Exception as exc:
            self.logger.critical(f"Unexpected error during token execution: {str(exc)}", exc_info=True)
            self.tx.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail='Internal Server Error'
            )


