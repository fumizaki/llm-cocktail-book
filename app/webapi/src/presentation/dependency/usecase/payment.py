from fastapi import Depends
from sqlalchemy.orm import Session
from src.presentation.dependency.authorization import get_credential_from_header
from src.application.payment import PaymentUsecase
from src.application.credential import Credential
from src.infrastructure.database.rdb import get_psql_session, TransactionClient


def implement_payment_usecase(
        credential: Credential = Depends(get_credential_from_header),
        session: Session = Depends(get_psql_session),
    ):
    return PaymentUsecase(
        credential,
        TransactionClient(session)
    )