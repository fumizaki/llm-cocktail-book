from fastapi import HTTPException, status
from .query import ChatbotMessageQuery
from .model import CreateChatbotMessageModel
from src.application.core import Credential
from src.domain.aggregate.chatbot import AggChatbot
from src.domain.entity.chatbot_message import ChatbotMessage
from src.domain.repository.chatbot_message import ChatbotMessageRepository
from src.infrastructure.database.rdb.transaction import TransactionClient
from src.infrastructure.llm.txt2txt import LLMTxt2TxtClient, Txt2TxtModel, Txt2TxtLLMMessageRole, Txt2TxtLLMMessage
from src.infrastructure.logging import JsonLineLoggingClient

class ChatbotMessageUsecase:
    def __init__(
        self,
        credential: Credential,
        tx: TransactionClient,
        chatbot_message_query: ChatbotMessageQuery,
        chatbot_message_repository: ChatbotMessageRepository
    ) -> None:
        self.credential = credential
        self.tx = tx
        self.chatbot_message_query = chatbot_message_query
        self.chatbot_message_repository = chatbot_message_repository
        self.logger = JsonLineLoggingClient.get_logger(self.__class__.__name__)


    async def get_all_exec(self, chatbot_id: str) -> AggChatbot:
        self.logger.info(f"Get All Chatbot Message execution started for account: {self.credential.account_id}")
        try:
            agg_chat_in_db: AggChatbot = self.chatbot_message_query.get_agg_chatbot(chatbot_id, self.credential.account_id)
            return agg_chat_in_db
        
        except HTTPException as http_exc:
            self.logger.error(f"HTTPException occurred: {http_exc.detail}")
            raise

        except Exception as exc:
            self.logger.critical(f"Unexpected error during token execution: {str(exc)}", exc_info=True)
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail='Internal Server Error'
            )



    async def create_exec(self, params: CreateChatbotMessageModel) -> ChatbotMessage:
        self.logger.info(f"Create Chatbot Message execution started for account: {self.credential.account_id}")

        try:
            self.logger.info(f"Get messages as context in CHatbot: {params.chatbot_id}")
            # コンテキストとして履歴を取得
            context_in_db: list[ChatbotMessage] = self.chatbot_message_repository.get_latest_list_exclude_deleted(params.chatbot_id, 6)

            self.logger.info(f"Create Message with prompt")
            # DBへ保存
            user_chatbot_message_in_db = self.chatbot_message_repository.create(ChatbotMessage(
                    chatbot_id=params.chatbot_id,
                    role=Txt2TxtLLMMessageRole.USER,
                    content=params.prompt
                ))
            
            self.logger.info(f"Create Message with LLM")
            txt2txt = LLMTxt2TxtClient()
            res = await txt2txt.generate(
                Txt2TxtModel(
                    meta=params.meta,
                    prompt=user_chatbot_message_in_db.content,
                    context=[Txt2TxtLLMMessage(prompt=message.content, role=message.role) for message in context_in_db]
                )
            )
            
            assistant_chatbot_message_in_db: ChatbotMessage = self.chatbot_message_repository.create(
                ChatbotMessage(
                    chatbot_id=params.chatbot_id,
                    role=Txt2TxtLLMMessageRole.ASSISTANT,
                    content=res.content
                ))
            
            self.tx.commit()
            
            return assistant_chatbot_message_in_db
            
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
