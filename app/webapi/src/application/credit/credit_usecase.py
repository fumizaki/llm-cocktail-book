from fastapi import HTTPException, status
from ..credential import Credential
from src.domain.credit import Credit, CreditRepository
from src.infrastructure.database.rdb import TransactionClient
from src.infrastructure.logging import JsonLineLoggingClient

class CreditUsecase:
    def __init__(
        self,
        credential: Credential,
        tx: TransactionClient,
        credit_repository: CreditRepository,
    ) -> None:
        self.credential = credential
        self.tx = tx
        self.credit_repository = credit_repository
        self.logger = JsonLineLoggingClient.get_logger(self.__class__.__name__)


    async def get_exec(self) -> Credit:
        
        self.logger.info(f"Get Credit execution started for account: {self.credential.account_id}")
        try:
            credit_in_db: Credit = self.credit_repository.get_exclude_deleted(self.credential.account_id)
            return credit_in_db
        
        except HTTPException as http_exc:
            self.logger.error(f"HTTPException occurred: {http_exc.detail}")
            raise

        except Exception as exc:
            self.logger.critical(f"Unexpected error during token execution: {str(exc)}", exc_info=True)
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail='Internal Server Error'
            )

