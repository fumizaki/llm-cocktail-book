from abc import ABC, abstractmethod
from .credit_transaction_entity import CreditTransaction


class CreditTransactionRepository(ABC):

    @abstractmethod
    def get_exclude_deleted(self, account_id: str) -> CreditTransaction:
        raise NotImplementedError

    @abstractmethod
    def create(self, entity: CreditTransaction) -> CreditTransaction:
        raise NotImplementedError
    
    @abstractmethod
    def delete(self, id: str) -> CreditTransaction:
        raise NotImplementedError
    
    
    
    
    