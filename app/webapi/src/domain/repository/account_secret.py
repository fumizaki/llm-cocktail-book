from abc import ABC, abstractmethod
from src.domain.entity.account_secret import AccountSecret
from src.domain.schema.account_secret import UpdateAccountSecretParams


class AccountSecretRepository(ABC):

    @abstractmethod
    def get_exclude_deleted(self, account_id: str) -> AccountSecret:
        raise NotImplementedError

    @abstractmethod
    def create(self, entity: AccountSecret) -> AccountSecret:
        raise NotImplementedError
    
    @abstractmethod
    def update(self, id: str, password: str, salt: str, stretching: int) -> AccountSecret:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: str) -> AccountSecret:
        raise NotImplementedError
    
    
    
    
    