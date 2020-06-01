from .models import Game
import django_filters

class GameFilter(django_filters.FilterSet):
    class Meta:
        model = Game
        fields = ['category']
