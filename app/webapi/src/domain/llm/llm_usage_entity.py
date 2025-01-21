from ..entity import Entity


class LLMUsage(Entity):
    account_id: str
    resource: str
    model: str
    task: str
    usage: int

