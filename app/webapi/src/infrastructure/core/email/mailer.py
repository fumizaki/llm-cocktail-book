from abc import ABC, abstractmethod
from src.infrastructure.core.email.content import EmailContent


class EmailClient(ABC):

    @abstractmethod
    def send_mail(self, to_add: list[str], content: EmailContent) -> None:
        raise NotImplementedError