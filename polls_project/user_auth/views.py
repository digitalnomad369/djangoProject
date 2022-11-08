import re
from tkinter import NO
from django.shortcuts import HttpResponseRedirect, render
from django.contrib.auth import authenticate, login
from django.urls import reverse

# Create your views here.
def user_login(request):
    return render(request, 'authentication/login.html')

def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user is None:
        return HttpResponseRedirect(
            reverse('user_auth:login')
        )
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('user_auth:show_user')
        )


def show_user(request):
    print(request.user.username)
    return render(request, 'authentication/user.html', {
        'username': request.user.username,
        'password': request.user.password
    })

