import logging

from sqlalchemy import create_engine, event, inspect, text
from sqlalchemy.orm import declarative_base, sessionmaker

import config

log = logging.getLogger("wisein.db")

DB_PATH = config.BACKEND_DIR / "wisein.db"


def _database_url() -> str:
    url = config.DATABASE_URL
    if url:
        # Neon/Vercel hand out postgres:// URLs; use the psycopg (v3) driver.
        for prefix in ("postgres://", "postgresql://"):
            if url.startswith(prefix):
                return "postgresql+psycopg://" + url[len(prefix):]
        return url
    if config.ON_VERCEL:
        log.warning("DATABASE_URL is not set: using a temporary SQLite file in /tmp. Conversations, tickets and "
                    "articles will NOT persist. Connect a Postgres database (Vercel > Storage > Neon).")
        return "sqlite:////tmp/wisein.db"
    return f"sqlite:///{DB_PATH}"


SQLALCHEMY_DATABASE_URL = _database_url()
IS_SQLITE = SQLALCHEMY_DATABASE_URL.startswith("sqlite")

if IS_SQLITE:
    engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False, "timeout": 15})

    @event.listens_for(engine, "connect")
    def _sqlite_pragmas(dbapi_conn, _record):
        cur = dbapi_conn.cursor()
        cur.execute("PRAGMA journal_mode=WAL")    # readers don't block the chat writer
        cur.execute("PRAGMA synchronous=NORMAL")  # fast commits; safe with WAL
        cur.close()
else:
    # Serverless-friendly pool: small, verified before use, recycled before the server drops idle connections.
    engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_size=3, max_overflow=5, pool_pre_ping=True, pool_recycle=240)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, expire_on_commit=False)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    """Create missing tables and add columns introduced after an existing DB was created.
    Safe to run concurrently from several cold-starting instances."""
    import models  # noqa: F401  (registers tables)

    for attempt in range(3):
        try:
            Base.metadata.create_all(bind=engine)
            insp = inspect(engine)
            with engine.begin() as conn:
                for table in Base.metadata.sorted_tables:
                    existing = {c["name"] for c in insp.get_columns(table.name)}
                    for col in table.columns:
                        if col.name not in existing:
                            coltype = col.type.compile(dialect=engine.dialect)
                            conn.execute(text(f'ALTER TABLE "{table.name}" ADD COLUMN "{col.name}" {coltype}'))
                            log.info("Migrated: added column %s.%s", table.name, col.name)
            return
        except Exception as e:  # another instance created the same table/column at the same moment
            if attempt == 2:
                raise
            log.warning("init_db retry after: %s", e)
