from datetime import datetime
from sqlalchemy import DateTime, String
from sqlalchemy.orm import DeclarativeBase, declared_attr, mapped_column, Mapped
from sqlalchemy.sql import func
from uuid import uuid4

class TimestampMixin:
    
    @declared_attr
    def created_at(cls) -> Mapped[datetime]:
        return mapped_column(
            DateTime,
            default = func.now(),
            nullable = False
        )
    
    @declared_attr
    def updated_at(cls) -> Mapped[datetime]:
        return mapped_column(
            DateTime,
            default = func.now(),
            onupdate = func.now(),
            nullable = False
        )
    
    @declared_attr
    def deleted_at(cls) -> Mapped[datetime]:
        return mapped_column(
            DateTime,
            nullable = True
        )

    def now():
        return func.now()



class CoreTable(DeclarativeBase, TimestampMixin):

    @declared_attr
    def id(cls) -> Mapped[str]:
        return mapped_column(
            String,
            default = lambda: str(uuid4()),
            primary_key=True,
            nullable = False
        )


