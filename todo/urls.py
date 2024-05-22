from django.urls import path
from .views import (
    index,
    add_task,
    tag_list,
    update_tag,
    delete_tag,
    add_tag,
    update_task,
    delete_task,
    toggle_task_status,
)

urlpatterns = [
    path("", index, name="index"),
    path("add_task/", add_task, name="add_task"),
    path("add_tag/", add_tag, name="add_tag"),
    path("tag/list/", tag_list, name="tag_list"),
    path("tag/update/<int:pk>/", update_tag, name="update_tag"),
    path("tag/delete/<int:pk>/", delete_tag, name="delete_tag"),
    path("task/update/<int:pk>/", update_task, name="update_task"),
    path("task/delete/<int:pk>/", delete_task, name="delete_task"),
    path("task/toggle/<int:pk>/", toggle_task_status, name="toggle_task_status"),
]

app_name = "todo"
