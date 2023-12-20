from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Example additional fields
    timezone = models.CharField(max_length=50, default='UTC')
    daily_reminder_time = models.TimeField(null=True, blank=True)  # Optional field for daily reminders
    weekly_summary = models.BooleanField(default=True)  # Whether the user wants a weekly summary

    def __str__(self):
        return self.user.username
