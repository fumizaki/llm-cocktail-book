from src.domain.entity.core import CoreEntity


class LLMUsage(CoreEntity):
    account_id: str
    resource: str
    model: str
    task: str
    usage: int

