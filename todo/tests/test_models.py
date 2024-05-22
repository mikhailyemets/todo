from django.test import TestCase
from ..models import Task, Tag


class TaskModelTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        Task.objects.create(content='Test Task', is_done=False)

    def test_content_label(self):
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field('content').verbose_name
        self.assertEqual(field_label, 'content')

    def test_is_done_default_value(self):
        task = Task.objects.get(id=1)
        self.assertFalse(task.is_done)


class TagModelTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        Tag.objects.create(name='Test Tag')

    def test_name_label(self):
        tag = Tag.objects.get(id=1)
        field_label = tag._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_object_name_is_name(self):
        tag = Tag.objects.get(id=1)
        expected_object_name = tag.name
        self.assertEqual(str(tag), expected_object_name)
