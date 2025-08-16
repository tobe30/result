from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Result
from django.conf import settings

@receiver(post_save, sender=Result)
def send_result_notification(sender, instance, created, **kwargs):
    if created:  # Only send email when result is first created
        student = instance.student
        course = instance.course

        subject = "Your Result Has Been Uploaded"
        message = f"""
Hello {student.name},

Your result for {course.name} ({course.code}) has been uploaded.
You can now log in to your student portal to check your result.

Regards,
University Admin
        """
        recipient = [student.email]

        # Wrap the email sending inside try/except
        try:
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                recipient,
                fail_silently=False,
            )
        except Exception as e:
            print("Email failed:", e)
