from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from ..models import Task, Tag
from ..forms import TaskForm, TagForm

User = get_user_model()


class TaskViewsTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        cls.task = Task.objects.create(
            content="Test Task", is_done=False, owner=cls.user
        )
        cls.tag = Tag.objects.create(name="Test Tag")

    def test_index_view(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("todo:index"))
        self.assertEqual(response.status_code, 200)

    def test_add_task_view(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("todo:add_task"))
        self.assertEqual(response.status_code, 200)

    def test_add_task_form(self):
        form_data = {
            "content": "Test Task",
            "deadline": "2022-12-31 23:59:59",
            "is_done": False,
            "tags": [],
            "owner": self.user.id,
        }
        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_add_tag_view(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("todo:add_tag"))
        self.assertEqual(response.status_code, 200)

    def test_add_tag_form(self):
        form_data = {"name": "Test Tag"}
        form = TagForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_update_tag_view(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("todo:update_tag", kwargs={"pk": self.tag.id})
        )
        self.assertEqual(response.status_code, 200)

    def test_delete_tag_view(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("todo:delete_tag", kwargs={"pk": self.tag.id})
        )
        self.assertEqual(response.status_code, 302)

    def test_update_task_view(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("todo:update_task", kwargs={"pk": self.task.id})
        )
        self.assertEqual(response.status_code, 200)

    def test_delete_task_view(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("todo:delete_task", kwargs={"pk": self.task.id})
        )
        self.assertEqual(response.status_code, 302)

    def test_toggle_task_status_view(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("todo:toggle_task_status", kwargs={"pk": self.task.id})
        )
        self.assertEqual(response.status_code, 302)
