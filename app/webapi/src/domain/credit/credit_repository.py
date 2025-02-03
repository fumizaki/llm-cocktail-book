from abc import ABC, abstractmethod
from .credit_entity import Credit


class CreditRepository(ABC):

    @abstractmethod
    def get_exclude_deleted(self, account_id: str) -> Credit:
        raise NotImplementedError

    @abstractmethod
    def create(self, entity: Credit) -> Credit:
        raise NotImplementedError
    
    @abstractmethod
    def charge(self, account_id: str, balance: int) -> Credit:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: str) -> Credit:
        raise NotImplementedError
    
    
    
    
    