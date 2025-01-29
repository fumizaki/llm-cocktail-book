from fastapi import Depends
from sqlalchemy.orm import Session
from src.domain.credit import CreditRepository, CreditOrderRepository
from src.infrastructure.database.rdb import get_psql_session, CreditRepositoryImpl, CreditOrderRepositoryImpl


def implement_credit_repository(session: Session = Depends(get_psql_session)) -> CreditRepository:
    return CreditRepositoryImpl(session)


def implement_credit_order_repository(session: Session = Depends(get_psql_session)) -> CreditOrderRepository:
    return CreditOrderRepositoryImpl(session)
