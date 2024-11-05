from typing import Optional
from enum import Enum
from pydantic import BaseModel


class CoreSchema(BaseModel):
    class ConfigDict:
        frozen = True
        from_attributes = True
        arbitrary_types_allowed = True
        validate_assignment = True


class Sort(str, Enum):
    UPDATE = 'updated_at'
    CREATE = 'created_at'


class Order(str, Enum):
    DESC = 'desc'
    ASC = 'asc'


class SearchQueryParams(CoreSchema):
    q: Optional[str]
    sort: Sort
    order: Order
    page: int
    limit: int


class DefaultSearchQueryParams:
    q: Optional[str] = None
    sort: Sort = Sort.UPDATE
    order: Order = Order.DESC
    page: int = 1
    limit: int = 9