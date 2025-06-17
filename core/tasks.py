from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_welcome_email(email, username):
    """
    Asynchronous task to send a welcome email to the user.
    Uses Django's send_mail function and Celery worker.
    """
    if not email:
        return
    try:
        send_mail(
            "Welcome!",
            f"Hi {username}, thank you for registering! Welcome to our platform.",
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
    except Exception as e:
        print(f"Error sending email: {e}")
