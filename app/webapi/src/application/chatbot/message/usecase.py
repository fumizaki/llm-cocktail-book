from .query import ChatbotMessageQuery
from .model import CreateChatbotMessageModel
from src.application.core import Credential
from src.domain.aggregate.chatbot import AggChatbot
from src.domain.entity.chatbot_message import ChatbotMessage
from src.infrastructure.database.rdb.transaction import TransactionClient
from src.infrastructure.llm.txt2txt import LLMTxt2TxtClient, Txt2TxtModel, Txt2TxtLLMMessageRole

class ChatbotMessageUsecase:
    def __init__(
        self,
        credential: Credential,
        tx: TransactionClient,
        chatbot_message_query: ChatbotMessageQuery
    ) -> None:
        self.credential = credential
        self.tx = tx
        self.chatbot_message_query = chatbot_message_query


    def get_all_exec(self, chatbot_id: str) -> AggChatbot:
        try:
            agg_chat_in_db: AggChatbot = self.chatbot_message_query.get_agg_chatbot(chatbot_id, self.credential.account_id)
            return agg_chat_in_db
        finally:
            self.tx.close()


    async def create_exec(self, chatbot_id: str, params: CreateChatbotMessageModel) -> ChatbotMessage:
        try:
            txt2txt_client = LLMTxt2TxtClient()
            res = await txt2txt_client.generate(
                Txt2TxtModel(
                    mode=params.mode,
                    meta=params.meta,
                    prompt=params.prompt,
                    context=params.context
                )
            )
            print(res.usage)

            # DBへ保存
            user_chatbot_message = ChatbotMessage(
                    chatbot_id=chatbot_id,
                    role=Txt2TxtLLMMessageRole.USER,
                    content=params.prompt
                )
            
            assistant_chatbot_message = ChatbotMessage(
                    chatbot_id=chatbot_id,
                    role=Txt2TxtLLMMessageRole.ASSISTANT,
                    content=res.content
                )
            
            return assistant_chatbot_message
            
        except Exception as e:
            print(e)
            self.tx.rollback()
        finally:
            self.tx.close()
