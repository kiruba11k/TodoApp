from django.test import TestCase, Client
from django.contrib.auth.models import User
from TodoApp.models import Task


class TaskIntegrationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='Admin', password='Admin')

    def test_create_and_retrieve_task(self):
        # Test creating a task and retrieving it
        self.client.login(username='Admin', password='Admin')
        response = self.client.post('/task-create/', {'title': 'Test Task', 'description': 'Test Description'})
        self.assertEqual(response.status_code, 302)  # Assuming successful creation redirects to another page

        response = self.client.get('/tasks/')
        self.assertContains(response, 'Test Task')
