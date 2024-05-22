from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    """View function for the home page of the site."""

    return render(request, "todo/index.html")
