
from django.shortcuts import render, redirect
from .forms import ReminderForm
from .tasks import send_reminder_email
from datetime import timedelta
from django.utils import timezone
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage
from email_task_scheduler import settings
import pytz,os

def schedule_email(request):
    if request.method == 'POST':
        form = ReminderForm(request.POST, request.FILES)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            recipient_email = form.cleaned_data['recipient_email']
            scheduled_time = form.cleaned_data['scheduled_time']
            priority = form.cleaned_data['priority']
            attachment = request.FILES.get('attachment')
            cc_email = form.cleaned_data['cc_email']
            bcc_email = form.cleaned_data['bcc_email']
            email_format = form.cleaned_data['email_format']

            # Calculate the delay in seconds for the email to be sent at the chosen time
            now = timezone.now()
            delay = (scheduled_time - now).total_seconds()

            # desktop_file_path = r"C:\Users\Abdullah Rashad B S\Pictures\Screenshots\Screenshot (1).png"
            
            # # Check if the file exists before proceeding
            # if not os.path.exists(desktop_file_path):
            #     return HttpResponse("File not found!")
            
            if attachment:
                fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'attachments'))
                filename = fs.save(attachment.name, attachment)
                attachment_path = fs.path(filename)
            else:
                attachment_path = None  
            
            # Schedule the task
            send_reminder_email.apply_async(
                args=[subject, message, recipient_email,attachment_path, cc_email, bcc_email,  email_format],
                countdown=delay,
                priority={'low': 10, 'medium': 5, 'high': 0}[priority.lower()],  # Set priority in Celery
            )
            
            return redirect('success')
    else:
        form = ReminderForm()

    return render(request, 'scheduler/schedule_email.html', {'form': form})

from django.http import HttpResponse

def success(request):
    return HttpResponse("Success!")
