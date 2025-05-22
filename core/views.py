from django.shortcuts import render
from .models import *

def index(request):
    return render(request , 'index.html')

def letsgo(request):
    return render(request , 'letsgo.html')

def question(request):
    return render(request , 'question.html')

def discribe(request):
    return render(request , 'discribe.html')

def time(request):
    return render(request , 'time.html')

def info(reqeuest):
    return render(reqeuest , 'info.html')