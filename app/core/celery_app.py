from celery import Celery
from os import getenv

REDIS_URL = getenv("REDIS_URL")

celery = Celery(
    "ecommerce",
    broker=REDIS_URL,
    backend=REDIS_URL,
    include=[
        "app.tasks.order_tasks"
    ]
)

celery.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True
)