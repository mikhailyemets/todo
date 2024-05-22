from django.test import TestCase
from ..models import Task, Tag
from ..forms import TaskForm, TagForm, TaskUpdateForm
from django.contrib.auth import get_user_model


class TaskFormTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser", password="testpassword"
        )

    def test_task_form_valid(self):
        form_data = {
            "content": "Test Task",
            "deadline": "2022-12-31 23:59:59",
            "is_done": False,
            "tags": [],
            "owner": self.user.id,
        }
        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_tag_form_valid(self):
        form_data = {"name": "Test Tag"}
        form = TagForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_task_form_invalid(self):
        form_data = {}
        form = TaskForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_tag_form_invalid(self):
        form_data = {}
        form = TagForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_task_update_form_valid(self):
        task = Task.objects.create(content="Test Task", is_done=False, owner=self.user)
        form_data = {
            "content": "Test Task Updated",
            "is_done": True,
            "deadline": "2022-12-31 23:59:59",
            "owner": self.user.id,
        }
        form = TaskUpdateForm(data=form_data, instance=task)
        self.assertTrue(form.is_valid())
