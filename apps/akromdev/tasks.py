from django.core.mail import send_mail
from celery import shared_task
from core.settings import EMAIL_HOST_USER


@shared_task
def send_email_task(subject, message, email):
    try:
        send_mail(subject, message, email, [EMAIL_HOST_USER])
    except Exception as ex:
        print(f"Error in sending email: {ex}")
