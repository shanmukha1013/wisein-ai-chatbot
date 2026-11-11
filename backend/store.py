"""Persistence for chat traffic: conversations, messages, escalation tickets and analytics events.
Every function opens its own short session and never raises, so a DB hiccup can't break a chat reply."""
from __future__ import annotations

import json
import logging
from datetime import datetime, timezone

from database import SessionLocal
from models import Conversation, EventLog, Message, SupportTicket

log = logging.getLogger("wisein.store")


def get_or_create_conversation(conversation_id: int | None, client_id: str, first_message: str) -> int | None:
    db = SessionLocal()
    try:
        if conversation_id:
            conv = db.get(Conversation, conversation_id)
            if conv and conv.client_id == client_id and conv.is_active:
                return conv.id
        conv = Conversation(client_id=client_id, title=first_message[:80] or "New Conversation",
                            updated_at=datetime.now(timezone.utc))
        db.add(conv)
        db.commit()
        return conv.id
    except Exception:
        log.exception("Could not create conversation")
        db.rollback()
        return None
    finally:
        db.close()


def save_exchange(conversation_id: int | None, user_text: str, answer: str, sources: list[dict],
                  latency_ms: int | None) -> int | None:
    """Stores the user message and the assistant answer; returns the assistant message id."""
    if not conversation_id:
        return None
    db = SessionLocal()
    try:
        db.add(Message(conversation_id=conversation_id, role="user", content=user_text))
        bot = Message(conversation_id=conversation_id, role="assistant", content=answer,
                      sources_json=json.dumps(sources), latency_ms=latency_ms)
        db.add(bot)
        conv = db.get(Conversation, conversation_id)
        if conv:
            conv.updated_at = datetime.now(timezone.utc)
        db.commit()
        return bot.id
    except Exception:
        log.exception("Could not save messages")
        db.rollback()
        return None
    finally:
        db.close()


def open_ticket(conversation_id: int | None, summary: str) -> int | None:
    """Opens a human-support ticket for the conversation (one open ticket per conversation)."""
    if not conversation_id:
        return None
    db = SessionLocal()
    try:
        existing = (db.query(SupportTicket)
                    .filter(SupportTicket.conversation_id == conversation_id, SupportTicket.status != "RESOLVED")
                    .first())
        if existing:
            return existing.id
        ticket = SupportTicket(conversation_id=conversation_id, issue_summary=summary[:500])
        db.add(ticket)
        db.commit()
        return ticket.id
    except Exception:
        log.exception("Could not open ticket")
        db.rollback()
        return None
    finally:
        db.close()


def log_event(event_type: str, **metadata):
    db = SessionLocal()
    try:
        db.add(EventLog(event_type=event_type, metadata_json=json.dumps(metadata, default=str)))
        db.commit()
    except Exception:
        log.exception("Could not log event %s", event_type)
        db.rollback()
    finally:
        db.close()


def set_feedback(message_id: int, client_id: str, rating: str | None) -> bool:
    db = SessionLocal()
    try:
        msg = db.get(Message, message_id)
        if not msg or msg.role != "assistant":
            return False
        conv = db.get(Conversation, msg.conversation_id)
        if not conv or conv.client_id != client_id:
            return False
        msg.feedback = rating
        db.commit()
        return True
    except Exception:
        log.exception("Could not save feedback")
        db.rollback()
        return False
    finally:
        db.close()
