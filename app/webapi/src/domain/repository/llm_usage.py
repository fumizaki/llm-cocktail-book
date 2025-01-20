from abc import ABC, abstractmethod
from src.domain.entity.llm_usage import LLMUsage


class LLMUsageRepository(ABC):

    @abstractmethod
    def get_exclude_deleted(self, id: str) -> LLMUsage:
        raise NotImplementedError
    
    @abstractmethod
    def get_all_exclude_deleted(self, account_id: str) -> list[LLMUsage]:
        raise NotImplementedError

    @abstractmethod
    def create(self, entity: LLMUsage) -> LLMUsage:
        raise NotImplementedError
    
    @abstractmethod
    def update(self) -> LLMUsage:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: str) -> LLMUsage:
        raise NotImplementedError
    