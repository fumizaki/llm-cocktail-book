from __future__ import annotations
from datetime import datetime
from uuid import uuid4
from sqlalchemy.orm import DeclarativeBase, declared_attr, mapped_column, Mapped
from sqlalchemy.sql import func
from sqlalchemy import String, Text, DateTime, Integer, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

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


class IdMixin:
    @declared_attr
    def id(cls) -> Mapped[str]:
        return mapped_column(
            String,
            default = lambda: str(uuid4()),
            primary_key=True,
            nullable = False
        )

class Table(DeclarativeBase, IdMixin, TimestampMixin):
    __abstruct__ = True


class AccountTable(Table):
    __tablename__ = 'account'
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True, index=True)
    email_verified: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    secret: Mapped[AccountSecretTable] = relationship('AccountSecretTable', uselist=False, viewonly=True)


class AccountSecretTable(Table):
    __tablename__ = 'account_secret'
    account_id: Mapped[str] = mapped_column(String, ForeignKey('account.id'))
    password: Mapped[str] = mapped_column(Text, nullable=False)
    salt: Mapped[str] = mapped_column(String(64), nullable=False)
    stretching: Mapped[int] = mapped_column(Integer, nullable=False)


class CreditTable(Table):
    __tablename__ = 'credit'
    account_id: Mapped[str] = mapped_column(String, ForeignKey('account.id'), unique=True)
    balance: Mapped[int] = mapped_column(Integer, nullable=False)


class CreditTransactionTable(Table):
    __tablename__ = 'credit_transaction'
    account_id: Mapped[str] = mapped_column(String, ForeignKey('account.id'))
    transaction_type: Mapped[str] = mapped_column(String(64), nullable=False)
    credit: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)


class CreditOrderTable(Table):
    __tablename__ = 'credit_order'
    account_id: Mapped[str] = mapped_column(String, ForeignKey('account.id'))
    provider: Mapped[str] = mapped_column(String(64), nullable=False)
    reference_id: Mapped[str] = mapped_column(Text, nullable=False)
    credit: Mapped[int] = mapped_column(Integer, nullable=False)
    amount: Mapped[int] = mapped_column(Integer, nullable=False) 
    currency: Mapped[str] = mapped_column(String(64), nullable=False)
    status: Mapped[str] = mapped_column(String(64), nullable=False)


class ChatbotTable(Table):
    __tablename__ = 'chatbot'
    account_id: Mapped[str] = mapped_column(String, ForeignKey('account.id'))
    title: Mapped[str] = mapped_column(String(64), nullable=False)
    messages: Mapped[list[ChatbotMessageTable]] = relationship('ChatbotMessageTable', viewonly=True)


class ChatbotMessageTable(Table):
    __tablename__ = 'chatbot_message'
    chatbot_id: Mapped[str] = mapped_column(String, ForeignKey('chatbot.id'))
    role: Mapped[str] = mapped_column(String, nullable=False)
    content: Mapped[str] = mapped_column(String, nullable=False)


class LLMUsageTable(Table):
    __tablename__ = 'llm_usage'
    account_id: Mapped[str] = mapped_column(String, ForeignKey('account.id'))
    resource: Mapped[str] = mapped_column(String(64), nullable=False)
    model: Mapped[str] = mapped_column(String(64), nullable=False)
    task: Mapped[str] = mapped_column(String(64), nullable=False)
    usage: Mapped[int] = mapped_column(Integer, nullable=False)


class WorkflowTable(Table):
    __tablename__ = 'workflow'
    account_id: Mapped[str] = mapped_column(String, ForeignKey('account.id'))
    title: Mapped[str] = mapped_column(String(64), nullable=False)
    status: Mapped[str] = mapped_column(String(64), nullable=False)
    jobs: Mapped[list[WorkflowJobTable]] = relationship('WorkflowJobTable', viewonly=True)


class WorkflowJobTable(Table):
    __tablename__ = 'workflow_job'
    workflow_id: Mapped[str] = mapped_column(String, ForeignKey('workflow.id'))
    on_success: Mapped[str] = mapped_column(String(64), nullable=True)
    on_failure: Mapped[str] = mapped_column(String(64), nullable=True)
    title: Mapped[str] = mapped_column(String(64), nullable=False)
    status: Mapped[str] = mapped_column(String(64), nullable=False)
    task: Mapped[str] = mapped_column(Text, nullable=False)
    

