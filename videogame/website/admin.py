from django.contrib import admin
from .models import Category, Article, Game, Favorite

admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Game)
admin.site.register(Favorite)