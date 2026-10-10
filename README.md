# Automated Product-Content Generation and Operations Workflow Engine

Portfolio-ready FastAPI/LLM workflow demonstrating Pydantic-validated structured output,
automated tone checks, PostgreSQL/Redis configuration, and Celery batch processing.

## Run
python -m venv .venv
pip install -r requirements.txt
copy .env.example .env
uvicorn app.main:app --reload

Celery:
celery -A app.worker.celery_app worker --loglevel=info

API docs: http://127.0.0.1:8000/docs

The resume metrics should only be presented as measured outcomes when backed by your
actual benchmark, production logs, or test records.
