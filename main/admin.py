from django.contrib import admin
from .models import Movie, Serie, Actor
# Register your models here.

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'imdb_rating', 'year']
    list_filter = ['category']
    search_fields = ['title']


@admin.register(Serie)
class SerieAdmin(admin.ModelAdmin):
    list_display = ['title', 'year']
    list_filter = ['category']
    search_fields = ['title']


admin.site.register(Actor)