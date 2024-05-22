from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from .forms import TaskForm, TagForm, TaskUpdateForm
from .models import Task, Tag


def index(request:HttpRequest) -> HttpResponse:
    tasks = Task.objects.all().prefetch_related('tags')
    context = {
        'tasks': tasks
    }
    return render(request, 'todo/index.html', context)


def add_task(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo:index')
    else:
        form = TaskForm()

    return render(request, 'todo/add_task.html', {'form': form})


def add_tag(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo:tag_list')
    else:
        form = TagForm()

    return render(request, 'todo/add_tag.html', {'form': form})


def tag_list(request: HttpRequest) -> HttpResponse:
    tags = Tag.objects.all()
    return render(request, 'todo/tag_list.html', {'tags': tags})


def update_tag(request: HttpRequest, pk: int) -> HttpResponse:
    tag = Tag.objects.get(id=pk)
    return redirect('todo:tag_list')


def delete_tag(request: HttpRequest, pk: int) -> HttpResponse:
    tag = Tag.objects.get(id=pk)
    tag.delete()
    return redirect('todo:tag_list')


def update_task(request:HttpRequest, pk: int) -> HttpResponse:
    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        form = TaskUpdateForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('todo:index')
    else:
        form = TaskUpdateForm(instance=task)

    return render(request, 'todo/update_task.html', {'form': form})


def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('todo:index')