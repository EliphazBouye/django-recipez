from django.http import HttpResponse
from django.shortcuts import render

from . import views


def home(request):
    return render(request, 'recipe/home.html', {})
