from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def index(request):
    if request.user.is_authenticated:
        return render(request, 'accounts/index.html')
    else:
        return redirect(log_user_in)


def reset(request):
    return render(request, 'accounts/reset.html')


def activate(request):
    return render(request, 'accounts/activate.html')


def log_user_in(request):
    if request.user.is_authenticated:
        return redirect(index)
    if 'username' in request.POST and 'password' in request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            success = 1
            return redirect(index)
        else:
            return render(request, 'accounts/login.html', {'failure': 1, 'username': username, 'password': password})
    else:
        return render(request, 'accounts/login.html', {'failure': 0})


def log_user_out(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect(log_user_in)

# Create your views here.
