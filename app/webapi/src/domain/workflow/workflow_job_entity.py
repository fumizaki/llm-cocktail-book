from typing import Optional
from ..entity import Entity


class WorkflowJob(Entity):
    workflow_id: str
    on_success: Optional[str] = None
    on_failure: Optional[str] = None
    title: str
    status: str
    task: str
    

