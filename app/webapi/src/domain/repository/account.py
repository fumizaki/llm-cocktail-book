from abc import ABC, abstractmethod
from src.domain.entity.account import Account


class AccountRepository(ABC):

    @abstractmethod
    def get_exclude_deleted(self, id: str) -> Account:
        raise NotImplementedError

    @abstractmethod
    def create(self, entity: Account) -> Account:
        raise NotImplementedError
    
    @abstractmethod
    def update(self) -> Account:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: str) -> Account:
        raise NotImplementedError
    
    
    
    
    