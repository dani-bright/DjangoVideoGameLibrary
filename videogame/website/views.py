from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth import authenticate, login as auth_login, logout
from .forms import LoginForm, RegisterForm
from functools import reduce
import operator
from django.contrib import messages
from django.urls import reverse
from website.models import Game, Article
from django.shortcuts import render, get_object_or_404
from .filters import GameFilter

def home(request):
    articles = Article.objects.all()
    return render(request, 'website/home.html', locals())

def search(request):
    articles = Article.objects.all()

    query = request.GET['q']
    if query:
        query_list = query.split()
        articles = articles.filter(
                reduce(operator.and_,
                       (Q(title__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(content__icontains=q) for q in query_list))
            )

    return render(request, 'website/search.html', locals())

def read(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'website/read.html', {'article':article})

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

def game(request):
    games = Game.objects.all()
    game_filter = GameFilter(request.GET, queryset=games)
    return render(request, 'website/game.html', {'filter': game_filter})