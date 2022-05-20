from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=64, blank=False, unique=True)
    year = models.PositiveSmallIntegerField(default=2000, blank=True, unique=False)
    description = models.TextField(default='')
    imdb_rating = models.DecimalField(
        max_digits=3, decimal_places=1, blank=True, null=True)
    poster = models.ImageField(upload_to='Django-Project-Assets', null=True, blank=True)
    category = models.CharField(max_length=10, blank=False, default='')

    def __str__(self):
        return self.title_with_year()
    

    def title_with_year(self):
        return f'{self.title} ({self.year})'


class Serie(models.Model):
    title = models.CharField(max_length=64, blank=False, unique=True)
    year = models.PositiveSmallIntegerField(default=2000, blank=True, unique=False)
    description = models.TextField(default='')
    poster = models.ImageField(upload_to='Django-Project-Assets', null=True, blank=True)
    category = models.CharField(max_length=10, blank=False, default='')

    def __str__(self):
        return self.title_with_year()
    

    def title_with_year(self):
        return f'{self.title} ({self.year})'


class Actor(models.Model):
    name = models.CharField(max_length=64, blank=False, unique=False)
    lastname = models.CharField(max_length=64, blank=True, unique=False)
    age = models.PositiveSmallIntegerField(default=20, blank=False, unique=True)
    universe = models.CharField(max_length=10, blank=False, default='')
    character = models.CharField(max_length=64, blank=False, unique=False, default='')
    photo = models.ImageField(upload_to='Django-Project-Assets', null=True, blank=True)
    movies = models.ManyToManyField(Movie, blank=True)
    series = models.ManyToManyField(Serie, blank=True)

    def __str__(self):
        return self.name_with_lastname()


    def name_with_lastname(self):
        return f'{self.name} {self.lastname}'