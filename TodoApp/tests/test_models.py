from django.test import TestCase
from django.utils import timezone
from rest_framework.exceptions import ValidationError
from TodoApp.models import Task


class TaskModelTest(TestCase):
    def test_due_date_validation(self):
        # Test due_date validation
        past_date = timezone.now() - timezone.timedelta(days=1)
        task = Task(title='Test Task', description='Test Description', due_date=past_date)
        with self.assertRaises(ValidationError):
            task.full_clean()
