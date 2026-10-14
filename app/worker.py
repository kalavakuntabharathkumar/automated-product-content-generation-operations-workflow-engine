from celery import Celery
import os

celery_app=Celery(
    "content",
    broker=os.getenv("REDIS_URL","redis://localhost:6379/0"),
    backend=os.getenv("REDIS_URL","redis://localhost:6379/0")
)

@celery_app.task
def generate_batch(products):
    return {"queued": len(products)}
