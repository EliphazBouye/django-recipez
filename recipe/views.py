from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    html = "<h1>Hello welcome to recipez app</h1>"
    return HttpResponse(html)