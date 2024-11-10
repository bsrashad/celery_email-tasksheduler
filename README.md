
# Task Scheduler and Email Notification System

This Django project allows users to schedule email reminders with customizable options, such as selecting the date and time, adding attachments, and setting the priority level. Background processing is handled by **Celery** with **Redis** as the message broker, enabling asynchronous task scheduling and reliable email delivery.

## Features

- **Schedule Emails**: Set a specific date and time for email reminders.
- **Priority Levels**: Choose the priority for tasks (Low, Medium, High).
- **Recurring Reminders**: Option to schedule emails on a recurring basis (Daily, Weekly, Monthly).
- **Attachments**: Attach files (e.g., PDFs, images) to email reminders.
- **CC/BCC Options**: Add additional recipients with CC and BCC fields.
- **Email Format**: Choose between Plain Text and HTML formats.
- **Task Progress Tracking**: Monitor background task status through the Celery worker logs.

## Tech Stack

- **Django** - Backend web framework
- **Celery** - Asynchronous task queue
- **Redis** - Message broker for Celery
- **SMTP** - Email sending (configurable to work with services like Gmail, SendGrid)

## Project Structure

```
task_scheduler/
│
├── task_scheduler/               # Django project folder
│   ├── __init__.py               # Initializes the project with Celery app
│   ├── celery.py                 # Celery configuration file
│   ├── settings.py               # Project settings (includes Celery and email settings)
│   ├── urls.py                   # Main URL configuration file
│
├── scheduler/                    # Django app for scheduling emails
│   ├── forms.py                  # Form for scheduling emails
│   ├── tasks.py                  # Celery task definitions for sending emails
│   ├── urls.py                   # URL configuration for the app
│   ├── views.py                  # Views for handling email scheduling and success display
│   └── templates/scheduler/      # HTML templates
│       ├── schedule_email.html   # Form to schedule email reminders
│       └── success.html          # Success page after scheduling email
│
├── manage.py                     # Django project management script
└── requirements.txt              # List of required packages
```

## Setup and Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/bsrashad/celery_email-tasksheduler.git
   cd celery_email-tasksheduler
   ```

2. **Install Dependencies**:

   Use the provided `requirements.txt` file to install the necessary packages.

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Redis**:

   Redis is required as the Celery message broker. You can install Redis using the following commands:
   
   - **Ubuntu**:
     ```bash
     sudo apt update
     sudo apt install redis-server
     ```
   - **MacOS**:
     ```bash
     brew install redis
     ```

   Make sure Redis is running:
   
   ```bash
   redis-server
   ```

4. **Configure Environment Variables**:

   Set up your email backend settings in `celery_email-tasksheduler/settings.py`. Here’s an example using Gmail:
   
   ```python
   EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
   EMAIL_HOST = 'smtp.gmail.com'
   EMAIL_PORT = 587
   EMAIL_USE_TLS = True
   EMAIL_HOST_USER = 'your-email@gmail.com'
   EMAIL_HOST_PASSWORD = 'your-email-password'
   
   DEFAULT_FROM_EMAIL = 'your-email@gmail.com'
   ```

5. **Run Database Migrations**:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Run Celery and Celery Beat**:

   Open separate terminals and start Celery worker and Celery beat:

  - Start Celery worker:
     ```bash
     celery -A celery_email-taskscheduler worker --loglevel=info
     ```
   - Start Celery beat (for periodic tasks):
     ```bash
     celery -A celery_email-taskscheduler beat --loglevel=info
     ```

7. **Start the Django Development Server**:

   ```bash
   python manage.py runserver
   ```

8. **Access the Application**:

   Open your browser and go to `http://127.0.0.1:8000/scheduler/schedule-email/` to schedule an email.

## Usage

1. **Schedule an Email**:
   - Navigate to the **Schedule Email** page.
   - Fill in the form with the following fields:
     - **Subject**: Email subject line.
     - **Message**: Content of the email.
     - **Recipient Email**: Email address to send the reminder.
     - **Scheduled Date and Time**: Exact date and time for the email to be sent.
     - **Priority**: Priority level for task processing (Low, Medium, High).
     - **Attachment** (optional): Upload a file to attach to the email.
     - **CC/BCC** (optional): Additional recipients for CC and BCC.
     - **Email Format**: Choose between Plain Text or HTML.
     - **Recurrence**: Set a one-time or recurring schedule for the reminder.
   
2. **View Scheduled Tasks**:
   - Celery workers process tasks in the background based on the scheduled date and time.
   - Check Celery worker logs for real-time status of tasks.



## Future Enhancements

- **Task Progress Tracking**: Real-time progress for each scheduled task.
- **User Authentication**: Allow users to log in and view/edit their scheduled reminders.
- **Recurring Reminders Customization**: Provide options for custom recurring intervals (e.g., every 3 days).
- **Reminder Dashboard**: Interface to list and manage scheduled reminders.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request if you’d like to improve the project.

