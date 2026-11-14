from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_welcome_email(email, username):
    send_mail(
        subject="Welcome to Our Online Library",
        message=f"""
Hello {username},

Thanks for joining our community!

Welcome to our Online Library.

We are happy to have you with us.

Happy Reading! 📚
""",
        from_email="thaju137112@gmail.com",
        recipient_list=[email],
    )

    return "Welcome email sent successfully"