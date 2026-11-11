import os

models_path = 'backend/models.py'
with open(models_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Add new tables for Memory, Analytics, Admin, Support
new_models = """
from sqlalchemy import ForeignKey, Text, Boolean

class Conversation(Base):
    __tablename__ = "conversations"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String, default="New Conversation")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    is_active = Column(Boolean, default=True)

class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    conversation_id = Column(Integer, ForeignKey("conversations.id"))
    role = Column(String) # user, assistant, system
    content = Column(Text)
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
    status = Column(String, default="DRAFT") # DRAFT, PUBLISHED, ARCHIVED
    content = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class SupportTicket(Base):
    __tablename__ = "support_tickets"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    conversation_id = Column(Integer, ForeignKey("conversations.id"))
    issue_summary = Column(String)
    status = Column(String, default="OPEN") # OPEN, IN_PROGRESS, RESOLVED
    created_at = Column(DateTime(timezone=True), server_default=func.now())
"""
if "class Conversation" not in content:
    content += new_models
    with open(models_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Models updated successfully.")
else:
    print("Models already exist.")
