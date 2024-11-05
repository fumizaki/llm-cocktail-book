from src.domain.entity.account import Account
from src.domain.entity.account_secret import AccountSecret

class AccountWithSecret(Account):
    secret: AccountSecret