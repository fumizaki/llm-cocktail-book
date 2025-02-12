from fastapi import Depends
from sqlalchemy.orm import Session
from src.presentation.dependency.authorization import get_credential_from_header
from src.presentation.dependency.repository.credit import implement_credit_repository, implement_credit_transaction_repository, implement_credit_order_repository
from src.application.credit import CreditUsecase, CreditTransactionUsecase, CreditOrderUsecase
from src.domain.account import AccountCredentialModel
from src.domain.credit import CreditRepository, CreditTransactionRepository, CreditOrderRepository
from src.infrastructure.database.rdb import get_psql_session, TransactionClient


def implement_credit_usecase(
        credential: AccountCredentialModel = Depends(get_credential_from_header),
        session: Session = Depends(get_psql_session),
        credit_repository: CreditRepository = Depends(implement_credit_repository)
    ):
    return CreditUsecase(
        credential,
        TransactionClient(session),
        credit_repository
    )

def implement_credit_transaction_usecase(
        credential: AccountCredentialModel = Depends(get_credential_from_header),
        session: Session = Depends(get_psql_session),
        credit_transaction_repository: CreditTransactionRepository = Depends(implement_credit_transaction_repository)
    ):
    return CreditTransactionUsecase(
        credential,
        TransactionClient(session),
        credit_transaction_repository
    )

def implement_credit_order_usecase(
        credential: AccountCredentialModel = Depends(get_credential_from_header),
        session: Session = Depends(get_psql_session),
        credit_order_repository: CreditOrderRepository = Depends(implement_credit_order_repository)
    ):
    return CreditOrderUsecase(
        credential,
        TransactionClient(session),
        credit_order_repository
    )