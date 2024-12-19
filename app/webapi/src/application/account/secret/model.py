from src.application.core.model import CoreModel

class UpdateAccountSecretModel(CoreModel):
    current_password: str
    new_password: str