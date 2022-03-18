from django.http import HttpResponse
from django.shortcuts import render

def say_Hello(request):
    return HttpResponse("Hello, World!")
