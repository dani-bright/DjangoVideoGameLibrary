from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect

def home(request):
    return render(request, 'website/home.html', locals())

def register(request):
    return render(request, 'website/register.html', locals())

def login(request):
    return render(request, 'website/login.html', locals())
