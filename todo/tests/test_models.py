from django.test import TestCase
from django.contrib.auth import get_user_model
from ..models import Task, Tag

User = get_user_model()


class TaskModelTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username="testuser", password="testpassword")
        Task.objects.create(content="Test Task", is_done=False, owner=user)

    def test_content_label(self):
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field("content").verbose_name
        self.assertEqual(field_label, "content")

    def test_is_done_default_value(self):
        task = Task.objects.get(id=1)
        self.assertFalse(task.is_done)

    def test_owner_not_null(self):
        task = Task.objects.get(id=1)
        self.assertIsNotNone(task.owner)

    def test_deadline_label(self):
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field("deadline").verbose_name
        self.assertEqual(field_label, "deadline")


class TagModelTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        Tag.objects.create(name="Test Tag")

    def test_name_label(self):
        tag = Tag.objects.get(id=1)
        field_label = tag._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    def test_object_name_is_name(self):
        tag = Tag.objects.get(id=1)
        expected_object_name = tag.name
        self.assertEqual(str(tag), expected_object_name)
