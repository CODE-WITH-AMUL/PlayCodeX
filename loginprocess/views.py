from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import login as login_user
from django.contrib import messages
from .models import *


def login(request):
    return render(request , 'account/login.html')

def register(request):
    return render(request , 'account/register.html')