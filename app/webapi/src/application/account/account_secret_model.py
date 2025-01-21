from ..model import Model

class UpdateAccountSecretModel(Model):
    current_password: str
    new_password: str