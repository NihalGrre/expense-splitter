# Expense Splitter

Split shared trip costs and settle up in the fewest payments.
Built with **FastAPI** and **PostgreSQL**.

> Status: Week 0 — project skeleton. Features, screenshots and a live link come later.

## Run it locally

You need **Python 3.11+**, **Git**, and **Docker Desktop** (for PostgreSQL).
No Docker? Install PostgreSQL 16 directly and create a user and database both
named `splitter` with password `splitter`.

```bash
# 1. Make a virtual environment and turn it on
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Settings: copy the example file
cp .env.example .env             # Windows: copy .env.example .env

# 4. Start PostgreSQL
docker compose up -d

# 5. Run the tests (both should pass)
pytest

# 6. Start the server, then open http://127.0.0.1:8000/docs
uvicorn app.main:app --reload
```

## Project layout

```
app/
  main.py      API endpoints
  db.py        database connection + session-per-request
tests/
  test_health.py
docker-compose.yml   local PostgreSQL
.env.example         settings template (copy to .env)
```

## How settling up works


