from django.test import TestCase
from TodoApp.forms import TaskForm


class TaskFormTest(TestCase):
    def test_clean_tags(self):
        # Test clean_tags method in TaskForm
        form = TaskForm(data={'tags': 'tag1, tag2'})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.clean_tags(), 'tag1, tag2')
