from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now, verbose_name="Date de parution")
    content = models.TextField()
    game = models.ForeignKey('Game', on_delete=models.CASCADE, null=True, blank = True)


    class Meta:
        verbose_name = "article"
        ordering = ['date']

    def __str__(self):
        return self.title

class Game(models.Model):
    title = models.CharField(max_length=100)
    editor = models.CharField(max_length=42)
    img = models.ImageField(null=False)
    description =models.TextField(null=False)
    releaseDate = models.DateTimeField(verbose_name="Date de parution")
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    class Meta:
        ordering = ['releaseDate']

    def __str__(self):
        return self.title

class Favorite(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    game = models.ForeignKey('Game', on_delete=models.CASCADE)