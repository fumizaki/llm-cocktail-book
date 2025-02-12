from fastapi import HTTPException, status
from src.domain.account import AccountCredentialModel
from src.domain.credit import CreditTransaction, CreditTransactionRepository
from src.infrastructure.database.rdb import TransactionClient
from src.infrastructure.logging import JsonLineLoggingClient

class CreditTransactionUsecase:
    def __init__(
        self,
        credential: AccountCredentialModel,
        tx: TransactionClient,
        credit_transaction_repository: CreditTransactionRepository,
    ) -> None:
        self.credential = credential
        self.tx = tx
        self.credit_transaction_repository = credit_transaction_repository
        self.logger = JsonLineLoggingClient.get_logger(self.__class__.__name__)


    async def get_all_exec(self) -> list[CreditTransaction]:
        
        self.logger.info(f"Get Credit Transaction execution started for account: {self.credential.account_id}")
        try:
            credit_transaction_in_db: CreditTransaction = self.credit_transaction_repository.get_all_exclude_deleted(self.credential.account_id)
            return credit_transaction_in_db
        
        except HTTPException as http_exc:
            self.logger.error(f"HTTPException occurred: {http_exc.detail}")
            raise

        except Exception as exc:
            self.logger.critical(f"Unexpected error during token execution: {str(exc)}", exc_info=True)
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail='Internal Server Error'
            )

