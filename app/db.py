"""Database setup: one engine for the whole app, one session per request.

- The *engine* manages the pool of connections to PostgreSQL.
- A *session* is a short-lived "conversation" with the database. Each API
  request gets its own session via get_db(), which closes it afterwards.
- Base is the parent class your tables (models) will inherit from in Week 1.
"""
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

load_dotenv()  # reads .env into environment variables

DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    "postgresql+psycopg://splitter:splitter@localhost:5432/splitter",
)

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False)


class Base(DeclarativeBase):
    """All models (User, Trip, Expense, ...) will subclass this in Week 1."""


def get_db():
    """FastAPI dependency: hand a session to an endpoint, then always close it."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
