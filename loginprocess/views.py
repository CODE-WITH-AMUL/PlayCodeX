from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_user
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login_user(request, user)
            messages.success(request, f'You have been logged in as {user.username}')
            return redirect('home')  
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')

    return render(request, 'account/login.html')


# Register View
def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get("conform_password")

        # Validation
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken')
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already taken')
            return redirect('register')

        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, f'User created successfully: {user.username}')
            return redirect('login')
        except Exception as e:
            messages.error(request, f'Error while creating user: {e}')
            return redirect('register')

    return render(request, 'account/register.html')


# Logout View
@login_required
def logout(request):
    messages.success(request, f'You have been logged out. See you soon, {request.user.username}!')
    auth_logout(request)
    return redirect('login')


# Terms and Conditions View
def treamandconduction(request):
    return render(request, 'account/tream.html')