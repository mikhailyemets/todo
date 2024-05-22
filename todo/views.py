from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import TaskForm, TagForm, TaskUpdateForm, SearchForm
from .models import Task, Tag


@login_required
def index(request: HttpRequest) -> HttpResponse:
    tag_search = request.GET.get("tag-search")
    tasks = Task.objects.all()

    if tag_search:
        tasks = tasks.filter(tags__name__icontains=tag_search)

    paginator = Paginator(tasks, 5)
    page = request.GET.get("page")

    try:
        tasks = paginator.page(page)
    except PageNotAnInteger:
        tasks = paginator.page(1)
    except EmptyPage:
        tasks = paginator.page(paginator.num_pages)

    context = {
        "tasks": tasks,
        "page_obj": tasks,
        "is_paginated": paginator.num_pages > 1,
    }

    return render(request, "todo/index.html", context)


def add_task(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todo:index")
    else:
        form = TaskForm()

    return render(request, "todo/add_task.html", {"form": form})


def add_tag(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todo:tag_list")
    else:
        form = TagForm()

    return render(request, "todo/add_tag.html", {"form": form})


def tag_list(request: HttpRequest) -> HttpResponse:
    tags = Tag.objects.all()
    return render(request, "todo/tag_list.html", {"tags": tags})


def update_tag(request: HttpRequest, pk: int) -> HttpResponse:
    tag = Tag.objects.get(id=pk)

    if request.method == "POST":
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            return redirect("todo:tag_list")
    else:
        form = TagForm(instance=tag)

    return render(request, "todo/update_tag.html", {"form": form, "tag": tag})


def delete_tag(request: HttpRequest, pk: int) -> HttpResponse:
    tag = Tag.objects.get(id=pk)
    tag.delete()
    return redirect("todo:tag_list")


def update_task(request: HttpRequest, pk: int) -> HttpResponse:
    task = Task.objects.get(id=pk)

    if request.method == "POST":
        form = TaskUpdateForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("todo:index")
    else:
        form = TaskUpdateForm(instance=task)

    return render(request, "todo/update_task.html", {"form": form})


def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect("todo:index")


def toggle_task_status(request: HttpRequest, pk: int) -> HttpResponse:
    task = Task.objects.get(id=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect("todo:index")
