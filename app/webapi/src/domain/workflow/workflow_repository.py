from abc import ABC, abstractmethod
from .workflow_entity import Workflow


class WorkflowRepository(ABC):

    @abstractmethod
    def get_exclude_deleted(self, id: str) -> Workflow:
        raise NotImplementedError
    
    @abstractmethod
    def get_all_exclude_deleted(self, account_id: str) -> list[Workflow]:
        raise NotImplementedError

    @abstractmethod
    def create(self, entity: Workflow) -> Workflow:
        raise NotImplementedError
    
    @abstractmethod
    def update_status(self, id: str, status: str) -> Workflow:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: str) -> Workflow:
        raise NotImplementedError
    