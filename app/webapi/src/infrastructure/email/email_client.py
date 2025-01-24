from abc import ABC, abstractmethod
from .email_model import (
    EmailModel, EmailResult
)


class EmailClient(ABC):

    @abstractmethod
    def send(self, params: EmailModel) -> EmailResult:
        raise NotImplementedError