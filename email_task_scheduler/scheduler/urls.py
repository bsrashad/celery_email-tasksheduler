# scheduler/urls.py

from django.urls import path
from .views import schedule_email, success

urlpatterns = [
    path('schedule-email/', schedule_email, name='schedule_email'),
    path('success/', success, name='success'),
]
