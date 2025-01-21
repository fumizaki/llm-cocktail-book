from ..entity import Entity

class AccountSecret(Entity):
    account_id: str
    password: str
    salt: str
    stretching: int