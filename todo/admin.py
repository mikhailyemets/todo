from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ("deadline",)
    list_filter = ("tags",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("name",)


admin.site.unregister(Group)
