from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('article/<int:id>/', views.read, name="read"),
    path('search/', views.search, name='search_results'),
    path('mylist/', views.myList),
    path('games/<int:idUser>/<int:idGame>/', views.favorite, name='addFavorite'),
    path('register/', views.register),
    path('login/', views.login),
    path('logout/', views.logout),
    path('games/', views.game),
    path('games/<int:id>/', views.gamesDetails, name="gamesDetails"),
]