from abc import ABC, abstractmethod
from .chatbot_graph_node_model import ChatbotGraphNode


class ChatbotGraphRepository(ABC):
    

    @abstractmethod
    def is_exists(self, chatbot_id: str) -> bool:
        raise NotImplementedError


    @abstractmethod
    def create(self, entity: ChatbotGraphNode) -> ChatbotGraphNode:
        raise NotImplementedError


    @abstractmethod
    def delete(self, chatbot_id: str) -> bool:
        raise NotImplementedError

    