from fastapi import HTTPException, status
from .model import CreateChatbotModel
from src.application.core import Credential
from src.domain.repository.chatbot import ChatbotRepository
from src.domain.entity.chatbot import Chatbot
from src.infrastructure.database.rdb.transaction import TransactionClient
from src.infrastructure.logging import JsonLineLoggingClient

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
        self.logger = JsonLineLoggingClient.get_logger(self.__class__.__name__)

    async def get_all_exec(self) -> list[Chatbot]:
        self.logger.info(f"Get All Chatbot execution started for account: {self.credential.account_id}")
        try:
            chatbot_in_db: list[Chatbot] = self.chatbot_repository.get_all_exclude_deleted(self.credential.account_id)
            return chatbot_in_db
        
        except HTTPException as http_exc:
            self.logger.error(f"HTTPException occurred: {http_exc.detail}")
            raise

        except Exception as exc:
            self.logger.critical(f"Unexpected error during token execution: {str(exc)}", exc_info=True)
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail='Internal Server Error'
            )



    async def create_exec(self, params: CreateChatbotModel) -> Chatbot:
        self.logger.info(f"Create Chatbot execution started for account: {self.credential.account_id}")
        try:
            result = self.chatbot_repository.create(Chatbot(
                account_id=self.credential.account_id,
                title=params.title
            ))
            self.tx.commit()
            return result
        
        except HTTPException as http_exc:
            self.logger.error(f"HTTPException occurred: {http_exc.detail}")
            self.tx.rollback()
            raise

        except Exception as exc:
            self.logger.critical(f"Unexpected error during token execution: {str(exc)}", exc_info=True)
            self.tx.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail='Internal Server Error'
            )