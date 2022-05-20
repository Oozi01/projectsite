from django.urls import path
from main.views import marvel_movies, new_marvel_movie, edit_marvel_movie, delete_marvel_movie
from main.views import marvel_series, new_marvel_serie, edit_marvel_serie, delete_marvel_serie
from main.views import marvel_actors, new_marvel_actor, edit_marvel_actor, delete_marvel_actor
from main.views import starwars_movies, new_starwars_movie, edit_starwars_movie, delete_starwars_movie
from main.views import starwars_series, new_starwars_serie, edit_starwars_serie, delete_starwars_serie
from main.views import starwars_actors, new_starwars_actor, edit_starwars_actor, delete_starwars_actor
from main.views import starwars_quiz, marvel_quiz

urlpatterns = [    
    path('swmovies/', starwars_movies, name='starwars_movies'),
    path('newstarwarsmovie/', new_starwars_movie, name='new_starwars_movie'),
    path('editstarwarsmovie/<int:id>/', edit_starwars_movie, name='edit_starwars_movie'),
    path('deletestarwarsmovie/<int:id>/', delete_starwars_movie, name='delete_starwars_movie'),

    path('swseries/', starwars_series, name='starwars_series'),
    path('newstarwarsserie/', new_starwars_serie, name='new_starwars_serie'),
    path('editstarwarsseries/<int:id>/', edit_starwars_serie, name='edit_starwars_serie'),
    path('deletestarwarsseries/<int:id>/', delete_starwars_serie, name='delete_starwars_serie'),

    path('swactors/', starwars_actors, name='starwars_actors'),
    path('newstarwarsactor/', new_starwars_actor, name='new_starwars_actor'),
    path('editstarwarsactor/<int:id>/', edit_starwars_actor, name='edit_starwars_actor'),
    path('deletestarwarsactor/<int:id>/', delete_starwars_actor, name='delete_starwars_actor'),

    path('starwarsquiz/', starwars_quiz, name='starwars_quiz'),



    path('mmovies/', marvel_movies, name='marvel_movies'),
    path('newmarvelmovie/', new_marvel_movie, name='new_marvel_movie'),
    path('editmarvelmovie/<int:id>/', edit_marvel_movie, name='edit_marvel_movie'),
    path('deletemarvelmovie/<int:id>/', delete_marvel_movie, name='delete_marvel_movie'),

    path('mseries/', marvel_series, name='marvel_series'),
    path('newmarvelserie/', new_marvel_serie, name='new_marvel_serie'),
    path('editmarvelserie/<int:id>/', edit_marvel_serie, name='edit_marvel_serie'),
    path('deletemarvelserie/<int:id>/', delete_marvel_serie, name='delete_marvel_serie'),

    path('mactors/', marvel_actors, name='marvel_actors'),
    path('newmarvelactor/', new_marvel_actor, name='new_marvel_actor'),
    path('editmarvelactor/<int:id>/', edit_marvel_actor, name='edit_marvel_actor'),
    path('deletemarvelactor/<int:id>/', delete_marvel_actor, name='delete_marvel_actor'),

    path('marvelquiz/', marvel_quiz, name='marvel_quiz'),

    
    
]
