from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class CustomUser(AbstractUser):
    # Fields from the original UserProfile
    timezone = models.CharField(max_length=50, default='UTC')
    daily_reminder_time = models.TimeField(null=True, blank=True)
    weekly_summary = models.BooleanField(default=True)

    # Additional fields
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # Any additional profile fields
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        unique_together = ('category', 'name')

    def __str__(self):
        return f"{self.category.name} - {self.name}"

class Activity(models.Model):
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    details = models.TextField(blank=True)

    class Meta:
        unique_together = ('subcategory', 'name')

    def __str__(self):
        return f"{self.subcategory.name} - {self.name}"
