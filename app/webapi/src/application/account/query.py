from abc import ABC, abstractmethod
from src.domain.aggregate.account import (
    AccountWithSecret,
)

class AccountQuery(ABC):
    
    @abstractmethod
    def get_account_with_secret(self, email: str) -> AccountWithSecret:
        raise NotImplementedError
    

