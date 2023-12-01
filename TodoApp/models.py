# models.py
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    due_date = models.DateField(null=True, blank=True)
    tags = models.CharField(max_length=200, default='', blank=True)
    status_choices = [
        ('OPEN', 'Open'),
        ('WORKING', 'Working'),
        ('DONE', 'Done'),
        ('OVERDUE', 'Overdue'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='OPEN', blank=False)

    def clean(self):
        # Ensure 'Due Date' is not before 'Timestamp created'
        if self.due_date and self.timestamp and self.due_date < self.timestamp.date():
            raise ValidationError("Due Date cannot be before Timestamp created.")

    def save(self, *args, **kwargs):
        # Set the timestamp here before saving
        if not self.timestamp:
            self.timestamp = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
