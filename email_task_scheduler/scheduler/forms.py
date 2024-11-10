# scheduler/forms.py

from django import forms
from django.core.exceptions import ValidationError
# from datetime import datetime
from django.utils import timezone

class ReminderForm(forms.Form):
    subject = forms.CharField(max_length=100, label='Subject')
    message = forms.CharField(widget=forms.Textarea, label='Message')
    recipient_email = forms.EmailField(label='Recipient Email')
    scheduled_time = forms.DateTimeField(label='Schedule Date and Time', widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    
    priority = forms.ChoiceField(choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], label='Priority')
    
    attachment = forms.FileField(required=False, label='Attachment (optional)')
    
    recurrence = forms.ChoiceField(
        choices=[
            ('none', 'One-time'), 
            ('daily', 'Daily'), 
            ('weekly', 'Weekly'), 
            ('monthly', 'Monthly')
        ], 
        label='Recurrence'
    )
    
    cc_email = forms.EmailField(required=False, label='CC Recipients (optional)', help_text="Separate multiple emails with commas.")
    bcc_email = forms.EmailField(required=False, label='BCC Recipients (optional)', help_text="Separate multiple emails with commas.")
    
    email_format = forms.ChoiceField(
        choices=[('plain', 'Plain Text'), ('html', 'HTML')], 
        label='Email Format'
    )

    category = forms.ChoiceField(
        choices=[('work', 'Work'), ('personal', 'Personal'), ('urgent', 'Urgent'), ('other', 'Other')], 
        label='Category'
    )
    
    # Optional: Add a clean method to ensure scheduled time is in the future
    def clean_scheduled_time(self):
        scheduled_time = self.cleaned_data['scheduled_time']
        if scheduled_time < timezone.now():
            raise ValidationError("The scheduled time cannot be in the past!")
        return scheduled_time
