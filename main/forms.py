from django.forms import ModelForm
from .models import Movie, Serie, Actor

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'year', 'imdb_rating', 'poster', 'category']


class SerieForm(ModelForm):
    class Meta:
        model = Serie
        fields = ['title', 'description', 'year', 'poster', 'category']


class ActorForm(ModelForm):
    class Meta:
        model = Actor
        fields = ['name', 'lastname', 'age', 'character', 'photo', 'movies', 'universe']
