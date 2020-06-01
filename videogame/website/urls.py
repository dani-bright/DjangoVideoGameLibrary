from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('article/<int:id>/', views.read, name="read"),
    path('register/', views.register),
    path('login/', views.login),
    path('logout/', views.logout),
]