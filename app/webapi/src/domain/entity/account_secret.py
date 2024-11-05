from src.domain.entity.core import CoreEntity

class AccountSecret(CoreEntity):
    account_id: str
    password: str
    salt: str
    stretching: int