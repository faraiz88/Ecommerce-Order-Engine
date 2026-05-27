from celery import Celery


celery = Celery(
    "ecommerce",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0",

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