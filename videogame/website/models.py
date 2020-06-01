from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(null=True, blank=True, upload_to="avatars/")

    def __str__(self):
        return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now, verbose_name="Date de parution")
    content = models.TextField(null=True)
    game = models.ForeignKey('Game', on_delete=models.CASCADE)


    class Meta:
        verbose_name = "article"
        ordering = ['date']

    def __str__(self):
        return self.title

class Game(models.Model):
    title = models.CharField(max_length=100)
    editor = models.CharField(max_length=42)
    img = models.TextField(null=True)
    description =models.TextField(null=False)
    releaseDate = models.DateTimeField(verbose_name="Date de parution")
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    class Meta:
        ordering = ['releaseDate']

    def __str__(self):
        return self.title

class Favorite(models.Model):
    user = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    game = models.ForeignKey('Game', on_delete=models.CASCADE)