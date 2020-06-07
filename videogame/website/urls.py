from django.urls import path
from . import views
from django.conf import settings
from django.contrib.auth.views import logout



urlpatterns = [
    path('', views.home, name="home"),
    path('article/<int:id>/', views.read, name="read"),
    path('search/', views.search, name='search_results'),
    path('games/<int:idUser>/<int:idGame>/', views.favorite, name='addFavorite'),
    path('register/', views.register),
    path('login/', views.login),
    path('logout/', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name="logout"),
    path('games/', views.game),
    path('games/<int:id>/', views.gamesDetails, name="gamesDetails"),
]