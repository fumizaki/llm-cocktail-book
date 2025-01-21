from enum import Enum

class WorkflowStatus(str, Enum):
    PENDING = 'pending'


class WorkflowJobStatus(str, Enum):
    PENDING = 'pending'
    