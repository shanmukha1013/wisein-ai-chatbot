import enum

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.sql import func

from database import Base


class Role(str, enum.Enum):
    USER = "USER"
    ADMIN = "ADMIN"
    SUPPORT_AGENT = "SUPPORT_AGENT"


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, default=Role.USER.value)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class Conversation(Base):
    __tablename__ = "conversations"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    client_id = Column(String, index=True)  # anonymous widget visitor id; guards access to the conversation
    title = Column(String, default="New Conversation")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True))
    is_active = Column(Boolean, default=True)


class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    conversation_id = Column(Integer, ForeignKey("conversations.id"), index=True)
    role = Column(String)  # user, assistant
    content = Column(Text)
    sources_json = Column(Text)
    latency_ms = Column(Integer)  # time to first answer token
    feedback = Column(String)  # up / down
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class EventLog(Base):
    __tablename__ = "event_logs"
    id = Column(Integer, primary_key=True, index=True)
    event_type = Column(String, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    metadata_json = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    topic = Column(String)
    status = Column(String, default="DRAFT")  # DRAFT, PUBLISHED, ARCHIVED
    content = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())


class SupportTicket(Base):
    __tablename__ = "support_tickets"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    conversation_id = Column(Integer, ForeignKey("conversations.id"))
    issue_summary = Column(String)
    status = Column(String, default="OPEN")  # OPEN, IN_PROGRESS, RESOLVED
    created_at = Column(DateTime(timezone=True), server_default=func.now())
