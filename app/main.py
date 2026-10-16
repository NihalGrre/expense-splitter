"""Entry point for the API.

Run it:   uvicorn app.main:app --reload
Then open http://127.0.0.1:8000/docs to try the endpoints in your browser.
"""
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import text
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import Session

from app.db import get_db

app = FastAPI(title="Expense Splitter")


@app.get("/")
def root():
    """Simplest possible endpoint: proves the server is running."""
    return {"message": "Expense Splitter API is running"}


@app.get("/health/db")
def health_db(db: Session = Depends(get_db)):
    """Proves the app can talk to PostgreSQL by running `SELECT 1`."""
    try:
        result = db.execute(text("SELECT 1")).scalar_one()
    except OperationalError:
        raise HTTPException(status_code=503, detail="Database unreachable")
    return {"database": "ok", "result": result}
