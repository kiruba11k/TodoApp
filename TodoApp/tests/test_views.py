# tests/test_views.py
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from TodoApp.views import TaskCreateView


class TaskCreateViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='Admin', password='Admin')

    def test_create_task_view(self):
        # Test TaskCreateView
        request = self.factory.post('/task-create/', {'title': 'Test Task', 'description': 'Test Description'})
        request.user = self.user
        response = TaskCreateView.as_view()(request)
        self.assertEqual(response.status_code, 302)  # Assuming successful creation redirects to another page
