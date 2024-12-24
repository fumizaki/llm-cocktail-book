from .model import CreateChatbotModel
from src.domain.repository.chatbot import ChatbotRepository
from src.domain.entity.credential import Credential
from src.domain.entity.chatbot import Chatbot
from src.infrastructure.database.rdb.transaction import TransactionClient

class ChatbotUsecase:
    def __init__(
        self,
        credential: Credential,
        tx: TransactionClient,
        chatbot_repository: ChatbotRepository,
    ) -> None:
        self.credential = credential
        self.tx = tx
        self.chatbot_repository = chatbot_repository

    def get_all_exec(self) -> list[Chatbot]:
        try:
            chatbot_in_db: list[Chatbot] = self.chatbot_repository.get_all_exclude_deleted(self.credential.id)
            return chatbot_in_db
        finally:
            self.tx.close()


    def create_exec(self, params: CreateChatbotModel) -> Chatbot:
        try:
            chat = Chatbot(
                account_id=self.credential.id,
                title=params.title
            )
            result = self.chatbot_repository.create(chat)
            self.tx.commit()
            return result
        
        except:
            self.tx.rollback()
        finally:
            self.tx.close()