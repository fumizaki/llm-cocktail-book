from abc import ABC, abstractmethod
from .credit_order_entity import CreditOrder


class CreditOrderRepository(ABC):

    @abstractmethod
    def get_exclude_deleted(self, account_id: str) -> CreditOrder:
        raise NotImplementedError

    @abstractmethod
    def create(self, entity: CreditOrder) -> CreditOrder:
        raise NotImplementedError
    
    @abstractmethod
    def update(self, id: str, status: str) -> CreditOrder:
        raise NotImplementedError
    
    @abstractmethod
    def delete(self, id: str) -> CreditOrder:
        raise NotImplementedError
    
    
    
    
    