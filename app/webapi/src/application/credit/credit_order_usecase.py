from fastapi import HTTPException, status
from ..credential import Credential
from .credit_order_model import CreateCreditOrderModel
from src.domain.credit import CreditOrder, CreditOrderRepository
from src.infrastructure.database.rdb import TransactionClient
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
        self.logger = JsonLineLoggingClient.get_logger(self.__class__.__name__)


    def create_exec(self, params: CreateCreditOrderModel) -> CreditOrder:
        
        self.logger.info(f"Get Credit execution started for account: {self.credential.account_id}")
        try:
            pass
        
        except HTTPException as http_exc:
            self.logger.error(f"HTTPException occurred: {http_exc.detail}")
            raise

        except Exception as exc:
            self.logger.critical(f"Unexpected error during token execution: {str(exc)}", exc_info=True)
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail='Internal Server Error'
            )

