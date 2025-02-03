from fastapi import HTTPException, status
from src.domain.credit import Credit, CreditRepository, CreditTransaction, CreditTransactionRepository, CreditOrder, CreditOrderRepository
from src.infrastructure.database.rdb import TransactionClient
from src.infrastructure.payment import StripePaymentIntentWebhook
from src.infrastructure.logging import JsonLineLoggingClient



class StripeWebhookUsecase:
    def __init__(
        self,
        stripe_webhook: StripePaymentIntentWebhook | None,
        tx: TransactionClient,
        credit_repository: CreditRepository,
        credit_transaction_repository: CreditTransactionRepository,
        credit_order_repository: CreditOrderRepository,
    ) -> None:
        self.stripe_webhook = stripe_webhook
        self.tx = tx
        self.credit_repository = credit_repository
        self.credit_transaction_repository = credit_transaction_repository
        self.credit_order_repository = credit_order_repository
        self.logger = JsonLineLoggingClient.get_logger(self.__class__.__name__)

    async def process_exec(self) -> None:
        try:
            if self.stripe_webhook is None:
                self.logger.info(f"このStripe Webhookは処理対象のイベントではないため、スキップします")
                return
            
            if self.stripe_webhook.event == 'payment_intent':
                credit_order_in_db: CreditOrder = self.credit_order_repository.update_by_reference('stripe', self.stripe_webhook.id, self.stripe_webhook.status)
                self.logger.info(f"Charge balance: {credit_order_in_db.credit} to account: {credit_order_in_db.account_id}")

                if credit_order_in_db.status == 'succeeded':
                    self.credit_transaction_repository.create(
                        CreditTransaction(
                            account_id=credit_order_in_db.account_id,
                            transaction_type='charge',
                            credit=credit_order_in_db.credit,
                            description='アプリ内課金'
                        )
                    )
                    credit_in_db: Credit = self.credit_repository.charge(credit_order_in_db.account_id, credit_order_in_db.credit)
                    self.logger.info(f"Credit balance: {credit_in_db.balance} of account: {credit_in_db.account_id}")

                    self.tx.commit()
                else:
                    return
            else:
                return
            
            return
        
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