"""Admin console API (analytics, conversations, tickets, knowledge management) and public feedback endpoint."""
import json
import logging
import statistics
import threading
import time
from collections import Counter
from datetime import datetime, timedelta, timezone
from typing import Literal, Optional

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import desc, func
from sqlalchemy.orm import Session

import store
from auth import get_current_admin, get_current_staff
from database import SessionLocal, get_db
from knowledge import kb
from models import Conversation, Document, EventLog, Message, SupportTicket, User

router = APIRouter(prefix="/api/features", tags=["features"])


# ---------------------------------------------------------------- public: feedback

class FeedbackIn(BaseModel):
    message_id: int
    client_id: str = Field(min_length=8, max_length=64)
    rating: Optional[Literal["up", "down"]] = None


@router.post("/feedback")
def feedback(body: FeedbackIn):
    if not store.set_feedback(body.message_id, body.client_id, body.rating):
        raise HTTPException(status_code=404, detail="Message not found")
    return {"success": True}


# ---------------------------------------------------------------- analytics

@router.get("/admin/analytics")
def get_analytics(db: Session = Depends(get_db), _: User = Depends(get_current_staff)):
    since = datetime.now(timezone.utc) - timedelta(days=14)
    recent_bot = (db.query(Message.latency_ms, Message.sources_json)
                  .filter(Message.role == "assistant").order_by(desc(Message.id)).limit(500).all())
    latencies = [m.latency_ms for m in recent_bot if m.latency_ms is not None]
    topics = Counter()
    for m in recent_bot:
        for s in json.loads(m.sources_json or "[]")[:1]:  # count the top source per answer
            topics[s.get("name", "")] += 1

    per_day = {str(day)[:10]: n for day, n in  # SQLite returns 'YYYY-MM-DD' strings, Postgres returns dates
               db.query(func.date(Conversation.created_at), func.count(Conversation.id))
               .filter(Conversation.created_at >= since).group_by(func.date(Conversation.created_at)).all()}
    days = [(datetime.now(timezone.utc) - timedelta(days=i)).strftime("%Y-%m-%d") for i in range(13, -1, -1)]
    unanswered = (db.query(EventLog).filter(EventLog.event_type == "no_answer")
                  .order_by(desc(EventLog.id)).limit(15).all())

    return {
        "total_conversations": db.query(Conversation).count(),
        "total_messages": db.query(Message).filter(Message.role == "user").count(),
        "open_tickets": db.query(SupportTicket).filter(SupportTicket.status != "RESOLVED").count(),
        "total_tickets": db.query(SupportTicket).count(),
        "feedback_up": db.query(Message).filter(Message.feedback == "up").count(),
        "feedback_down": db.query(Message).filter(Message.feedback == "down").count(),
        "avg_first_token_ms": round(statistics.mean(latencies)) if latencies else None,
        "median_first_token_ms": round(statistics.median(latencies)) if latencies else None,
        "conversations_per_day": [{"date": d, "count": per_day.get(d, 0)} for d in days],
        "top_topics": [{"topic": t, "count": c} for t, c in topics.most_common(8) if t],
        "recent_unanswered": [{"query": json.loads(e.metadata_json or "{}").get("query", ""), "created_at": e.created_at}
                              for e in unanswered],
        "events_breakdown": dict(db.query(EventLog.event_type, func.count(EventLog.id)).group_by(EventLog.event_type).all()),
        "knowledge_chunks": kb.size,
    }


# ---------------------------------------------------------------- conversations

@router.get("/admin/conversations")
def list_conversations(limit: int = 50, offset: int = 0, db: Session = Depends(get_db), _: User = Depends(get_current_staff)):
    limit = max(1, min(limit, 200))
    counts = (db.query(Message.conversation_id, func.count(Message.id))
              .filter(Message.role == "user").group_by(Message.conversation_id).subquery())
    rows = (db.query(Conversation, counts.c[1])
            .outerjoin(counts, counts.c.conversation_id == Conversation.id)
            .order_by(desc(func.coalesce(Conversation.updated_at, Conversation.created_at)))
            .offset(offset).limit(limit).all())
    ticketed = {t for (t,) in db.query(SupportTicket.conversation_id).all()}
    return [{
        "id": c.id, "title": c.title, "created_at": c.created_at, "updated_at": c.updated_at or c.created_at,
        "messages": n or 0, "escalated": c.id in ticketed,
    } for c, n in rows]


@router.get("/admin/conversations/{conv_id}")
def get_conversation(conv_id: int, db: Session = Depends(get_db), _: User = Depends(get_current_staff)):
    conv = db.get(Conversation, conv_id)
    if not conv:
        raise HTTPException(status_code=404, detail="Conversation not found")
    msgs = db.query(Message).filter(Message.conversation_id == conv_id).order_by(Message.id).all()
    return {
        "id": conv.id, "title": conv.title, "created_at": conv.created_at,
        "messages": [{
            "role": m.role, "content": m.content, "created_at": m.created_at, "feedback": m.feedback,
            "latency_ms": m.latency_ms, "sources": json.loads(m.sources_json or "[]"),
        } for m in msgs],
    }


# ---------------------------------------------------------------- tickets

class TicketUpdate(BaseModel):
    status: Literal["OPEN", "IN_PROGRESS", "RESOLVED"]


@router.get("/admin/tickets")
def list_tickets(db: Session = Depends(get_db), _: User = Depends(get_current_staff)):
    tickets = db.query(SupportTicket).order_by(desc(SupportTicket.created_at)).limit(500).all()
    return [{"id": t.id, "conversation_id": t.conversation_id, "issue": t.issue_summary,
             "status": t.status, "created_at": t.created_at} for t in tickets]


@router.patch("/admin/tickets/{ticket_id}")
def update_ticket(ticket_id: int, body: TicketUpdate, db: Session = Depends(get_db), _: User = Depends(get_current_staff)):
    ticket = db.get(SupportTicket, ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    ticket.status = body.status
    db.commit()
    return {"success": True}


# ---------------------------------------------------------------- knowledge management

class DocumentIn(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    topic: str = Field(default="", max_length=120)
    content: str = Field(min_length=1, max_length=200_000)
    status: Literal["DRAFT", "PUBLISHED"] = "DRAFT"


class DocumentUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=200)
    topic: Optional[str] = Field(default=None, max_length=120)
    content: Optional[str] = Field(default=None, min_length=1, max_length=200_000)
    status: Optional[Literal["DRAFT", "PUBLISHED", "ARCHIVED"]] = None


def _doc_out(d: Document) -> dict:
    return {"id": d.id, "title": d.title, "topic": d.topic, "status": d.status, "content": d.content,
            "created_at": d.created_at, "updated_at": d.updated_at}


def _sync_index(d: Document):
    if d.status == "PUBLISHED":
        kb.upsert_document(d.id, d.title, d.topic or d.title, d.content)
        _doc_versions[d.id] = str(d.updated_at)
    else:
        kb.remove_document(d.id)
        _doc_versions.pop(d.id, None)


@router.get("/admin/documents")
def list_documents(db: Session = Depends(get_db), _: User = Depends(get_current_admin)):
    return [_doc_out(d) for d in db.query(Document).order_by(desc(Document.updated_at)).all()]


@router.post("/admin/documents")
def create_document(body: DocumentIn, db: Session = Depends(get_db), _: User = Depends(get_current_admin)):
    doc = Document(title=body.title.strip(), topic=body.topic.strip(), content=body.content, status=body.status,
                   updated_at=datetime.now(timezone.utc))
    db.add(doc)
    db.commit()
    _sync_index(doc)
    return _doc_out(doc)


@router.patch("/admin/documents/{doc_id}")
def update_document(doc_id: int, body: DocumentUpdate, db: Session = Depends(get_db), _: User = Depends(get_current_admin)):
    doc = db.get(Document, doc_id)
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    for field, value in body.model_dump(exclude_none=True).items():
        setattr(doc, field, value.strip() if field in ("title", "topic") else value)
    doc.updated_at = datetime.now(timezone.utc)  # microsecond precision: other instances detect every edit
    db.commit()
    _sync_index(doc)
    return _doc_out(doc)


@router.delete("/admin/documents/{doc_id}")
def delete_document(doc_id: int, db: Session = Depends(get_db), _: User = Depends(get_current_admin)):
    doc = db.get(Document, doc_id)
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    db.delete(doc)
    db.commit()
    kb.remove_document(doc_id)
    _doc_versions.pop(doc_id, None)
    return {"success": True}


@router.post("/admin/reindex")
def reindex(_: User = Depends(get_current_admin)):
    """Reload the knowledge_base/ folder after editing its files (only changed chunks are re-embedded)."""
    kb.load()
    sync_published_documents(force=True)
    return {"success": True, "knowledge_chunks": kb.size}


# ---------------------------------------------------------------- keep every instance's index in sync
# Several server instances may run at once (serverless). Each checks the database at most every
# SYNC_SECONDS and (re)indexes only the published articles that were added, edited or removed.

SYNC_SECONDS = 15
_doc_versions: dict[int, str] = {}   # published doc id -> updated_at this instance has indexed
_sync_state = {"checked": 0.0}
_sync_lock = threading.Lock()


def sync_published_documents(force: bool = False):
    if not force and time.monotonic() - _sync_state["checked"] < SYNC_SECONDS:
        return
    with _sync_lock:
        if not force and time.monotonic() - _sync_state["checked"] < SYNC_SECONDS:
            return
        _sync_state["checked"] = time.monotonic()
        db = SessionLocal()
        try:
            current = {i: str(u) for i, u in db.query(Document.id, Document.updated_at)
                       .filter(Document.status == "PUBLISHED").all()}
            for doc_id in [i for i in _doc_versions if i not in current]:
                kb.remove_document(doc_id)
                _doc_versions.pop(doc_id, None)
            changed = [i for i, u in current.items() if _doc_versions.get(i) != u]
            if changed:
                for d in db.query(Document).filter(Document.id.in_(changed)).all():
                    kb.upsert_document(d.id, d.title, d.topic or d.title, d.content)
                    _doc_versions[d.id] = current[d.id]
        except Exception:
            logging.getLogger("wisein.features").exception("Published-article sync failed")
        finally:
            db.close()


def load_published_documents():
    """Called at startup so admin-published articles are searchable alongside the KB."""
    sync_published_documents(force=True)
