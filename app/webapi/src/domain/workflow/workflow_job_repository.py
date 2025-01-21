from abc import ABC, abstractmethod
from .workflow_job_entity import WorkflowJob


class WorkflowJobRepository(ABC):

    @abstractmethod
    def get_exclude_deleted(self, id: str) -> WorkflowJob:
        raise NotImplementedError
    
    @abstractmethod
    def get_all_exclude_deleted(self, workflow_id: str) -> list[WorkflowJob]:
        raise NotImplementedError

    @abstractmethod
    def create(self, entity: WorkflowJob) -> WorkflowJob:
        raise NotImplementedError
    
    @abstractmethod
    def update_status(self, id: str, status: str) -> WorkflowJob:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: str) -> WorkflowJob:
        raise NotImplementedError
    