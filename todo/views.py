from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Task, Tag


def index(request):
    tasks = Task.objects.all().prefetch_related('tags')
    context = {
        'tasks': tasks
    }
    return render(request, 'todo/index.html', context)
