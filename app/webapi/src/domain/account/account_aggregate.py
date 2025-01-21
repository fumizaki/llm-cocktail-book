from .account_entity import Account
from .account_secret_entity import AccountSecret

class AccountWithSecret(Account):
    secret: AccountSecret