from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect

def home(request):
    return render(request, 'website/home.html', locals())
