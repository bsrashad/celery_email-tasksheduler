# scheduler/tasks.py

from celery import shared_task
from django.core.mail import send_mail, EmailMessage
# from django.conf import settings
from email_task_scheduler import settings
import os
@shared_task
def send_reminder_email(subject, message, recipient_email,attachment_path, cc_email=None, bcc_email=None,  email_format='plain'):
    """
    Task to send a reminder email, with optional CC, BCC, and attachment.
    """
    email = EmailMessage(
        subject=subject,
        body=message,
        from_email=settings.EMAIL_HOST_USER,
        to=[recipient_email],
        cc=[cc_email] if cc_email else [],
        bcc=[bcc_email] if bcc_email else [],
    )
    
    if attachment_path and os.path.exists(attachment_path):
        email.attach_file(attachment_path)
    
    if email_format == 'html':
        email.content_subtype = "html"  # Set email format to HTML
    
    email.send(fail_silently=False)
    return "Email sent successfully!"
