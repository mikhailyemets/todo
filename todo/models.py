from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField("Tag", related_name="tasks", blank=True)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="tasks",
    )

    def __str__(self):
        return self.content

    class Meta:
        ordering = ["is_done"]


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
