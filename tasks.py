from celery import Celery
import time

celery = Celery(
    "tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

@celery.task
def send_email(email):

    print(f"Sending email to {email}")

    time.sleep(10)

    return f"Email sent to {email}"
