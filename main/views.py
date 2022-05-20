from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Movie, Serie, Actor
from .forms import MovieForm, SerieForm, ActorForm
from django.contrib.auth.decorators import login_required


def marvel_site(request):
    return render(request, 'marvelMain.html', {})

def marvel_movies(request):
    marvel = Movie.objects.filter(category='Marvel')
    return render(request, 'marvelmovies.html', {'movies': marvel})    

def marvel_series(request):
    marvel = Serie.objects.filter(category='Marvel')
    return render(request, 'marvelseries.html', {'series': marvel}) 

def marvel_actors(request):
    marvel = Actor.objects.filter(universe='Marvel')
    return render(request, 'marvelactors.html', {'actors': marvel})

def marvel_quiz(request):
    return render(request, 'marvelquiz.html', {})


@login_required
def new_marvel_movie(request):
    form = MovieForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(marvel_movies)

    return render(request, 'newmarvelmovie.html', {'form': form})

@login_required
def new_marvel_serie(request):
    form = SerieForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(marvel_series)

    return render(request, 'newmarvelserie.html', {'form': form})

@login_required
def new_marvel_actor(request):
    form = ActorForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(marvel_actors)

    return render(request, 'newmarvelactor.html', {'form': form})


@login_required
def edit_marvel_movie(request, id):
    movie = get_object_or_404(Movie, pk=id)
    form = MovieForm(request.POST or None, request.FILES or None, instance=movie)

    if form.is_valid():
        form.save()
        return redirect(marvel_movies)

    return render(request, 'editmarvelmovie.html', {'form': form})

@login_required
def edit_marvel_serie(request, id):
    serie = get_object_or_404(Serie, pk=id)
    form = SerieForm(request.POST or None, request.FILES or None, instance=serie)

    if form.is_valid():
        form.save()
        return redirect(marvel_series)

    return render(request, 'editmarvelserie.html', {'form': form})

@login_required
def edit_marvel_actor(request, id):
    actor = get_object_or_404(Actor, pk=id)
    form = ActorForm(request.POST or None, request.FILES or None, instance=actor)

    if form.is_valid():
        form.save()
        return redirect(marvel_actors)

    return render(request, 'editmarvelactor.html', {'form': form})

@login_required
def delete_marvel_movie(request, id):
    movie = get_object_or_404(Movie, pk=id)

    if request.method == 'POST':
        movie.delete()
        return redirect(marvel_movies)

    return render(request, 'deletemarvelmovie.html', {'serie': movie})

@login_required
def delete_marvel_serie(request, id):
    serie = get_object_or_404(Serie, pk=id)

    if request.method == 'POST':
        serie.delete()
        return redirect(marvel_series)

    return render(request, 'deletemarvelserie.html', {'serie': serie})

@login_required
def delete_marvel_actor(request, id):
    actor = get_object_or_404(Actor, pk=id)

    if request.method == 'POST':
        actor.delete()
        return redirect(marvel_actors)

    return render(request, 'deletemarvelactor.html', {'actor': actor})




def starwars_site(request):
    return render(request, 'starwarsMain.html', {})

def starwars_movies(request):
    starwars = Movie.objects.filter(category='Star Wars')
    return render(request, 'starwarsmovies.html', {'movies': starwars})

def starwars_series(request):
    starwars = Serie.objects.filter(category='Star Wars')
    return render(request, 'starwarsseries.html', {'series': starwars})

def starwars_actors(request):
    starwars = Actor.objects.filter(universe='Star Wars')
    return render(request, 'starwarsactors.html', {'actors': starwars})

def starwars_quiz(request):
    return render(request, 'starwarsquiz.html', {})


@login_required
def new_starwars_movie(request):
    form = MovieForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(starwars_movies)

    return render(request, 'newstarwarsmovie.html', {'form': form})

@login_required
def new_starwars_serie(request):
    form = SerieForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(starwars_series)

    return render(request, 'newstarwarsserie.html', {'form': form})

@login_required
def new_starwars_actor(request):
    form = ActorForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(starwars_actors)

    return render(request, 'newstarwarsactor.html', {'form': form})



@login_required
def edit_starwars_movie(request, id):
    movie = get_object_or_404(Movie, pk=id)
    form = MovieForm(request.POST or None, request.FILES or None, instance=movie)

    if form.is_valid():
        form.save()
        return redirect(starwars_movies)

    return render(request, 'editstarwarsmovie.html', {'form': form})


@login_required
def edit_starwars_serie(request, id):
    serie = get_object_or_404(Serie, pk=id)
    form = SerieForm(request.POST or None, request.FILES or None, instance=serie)

    if form.is_valid():
        form.save()
        return redirect(starwars_series)

    return render(request, 'editstarwarsserie.html', {'form': form})


@login_required
def edit_starwars_actor(request, id):
    actor = get_object_or_404(Actor, pk=id)
    form = ActorForm(request.POST or None, request.FILES or None, instance=actor)

    if form.is_valid():
        form.save()
        return redirect(starwars_actors)

    return render(request, 'editstarwarsactor.html', {'form': form})


@login_required
def delete_starwars_movie(request, id):
    movie = get_object_or_404(Movie, pk=id)

    if request.method == 'POST':
        movie.delete()
        return redirect(starwars_movies)

    return render(request, 'deletestarwarsmovie.html', {'movie': movie})

@login_required
def delete_starwars_serie(request, id):
    serie = get_object_or_404(Serie, pk=id)

    if request.method == 'POST':
        serie.delete()
        return redirect(starwars_series)

    return render(request, 'deletestarwarsserie.html', {'serie': serie})


@login_required
def delete_starwars_actor(request, id):
    actor = get_object_or_404(Actor, pk=id)

    if request.method == 'POST':
        actor.delete()
        return redirect(starwars_actors)

    return render(request, 'deletestarwarsactor.html', {'actor': actor})


def home(request):
    return render(request, 'home.html', {})
