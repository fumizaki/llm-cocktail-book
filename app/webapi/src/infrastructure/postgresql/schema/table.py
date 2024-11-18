from __future__ import annotations
from datetime import datetime
from sqlalchemy import String, Text, DateTime, Integer, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from src.infrastructure.postgresql.schema.core import CoreTable


class AccountTable(CoreTable):
    __tablename__ = 'account'
    email: Mapped[str] = mapped_column(Text, nullable=False)
    email_verified: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    secret: Mapped[AccountSecretTable] = relationship('AccountSecretTable', uselist=False, viewonly=True)


class AccountSecretTable(CoreTable):
    __tablename__ = 'account_secret'
    account_id: Mapped[str] = mapped_column(String, ForeignKey('account.id'))
    password: Mapped[str] = mapped_column(Text, nullable=False)
    salt: Mapped[str] = mapped_column(String(64), nullable=False)
    stretching: Mapped[int] = mapped_column(Integer, nullable=False)


class ChatRoomTable(CoreTable):
    __tablename__ = 'chat_room'
    account_id: Mapped[str] = mapped_column(String, ForeignKey('account.id'))
    title: Mapped[str] = mapped_column(String(64), nullable=False)


class ChatMessageTable(CoreTable):
    __tablename__ = 'chat_message'
    room_id: Mapped[str] = mapped_column(String, ForeignKey('chat_room.id'))
    role: Mapped[str] = mapped_column(String, nullable=False)
    content: Mapped[str] = mapped_column(String, nullable=False)