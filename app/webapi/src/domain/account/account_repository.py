from abc import ABC, abstractmethod
from datetime import datetime
from .account_entity import Account


class AccountRepository(ABC):

    @abstractmethod
    def get_exclude_deleted(self, id: str) -> Account:
        raise NotImplementedError

    @abstractmethod
    def create(self, entity: Account) -> Account:
        raise NotImplementedError
    
    @abstractmethod
    def verify(self, id: str, verified_at: datetime) -> Account:
        raise NotImplementedError

    @abstractmethod
    def update(self) -> Account:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: str) -> Account:
        raise NotImplementedError
    
    
    
    
    