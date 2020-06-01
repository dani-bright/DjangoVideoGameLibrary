from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from .forms import LoginForm, RegisterForm
from django.contrib import messages
from django.urls import reverse



def home(request):
    return render(request, 'website/home.html', locals())

def Logout(request):
    logout(request)
    return redirect('')

def register(request):
    error = False

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = User.objects.create_user(username,email, password)
            if user:
                messages.success(request, 'Votre user a bien été crée.')
                user.is_staff=False
                user.is_superuser=False
                user.last_name=last_name
                user.first_name=first_name
                user.save()
            else:
                messages.error(request, "l'user n'a pas pas pu etre crée.")

    else:
        form = RegisterForm()

    return render(request, 'website/register.html', locals())

def login(request):
    error = False

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                auth_login(request, user)
            else:
                error = True
    else:
        form = LoginForm()

    return render(request, 'website/login.html', locals())
