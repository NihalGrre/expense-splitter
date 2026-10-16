"""Run with:  pytest

TestClient calls your endpoints in-process, so the server doesn't need to be
running. The database test does need PostgreSQL up (docker compose up -d).
"""
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Expense Splitter API is running"}


def test_database_connection():
    response = client.get("/health/db")
    assert response.status_code == 200, (
        "Can't reach PostgreSQL. Is it running? Try: docker compose up -d"
    )
    assert response.json() == {"database": "ok", "result": 1}
