from django.shortcuts import render
from Watchmate.models import Movie
from django.http import JsonResponse


# Create your views here.
def movies_list(request):
    movies = Movie.objects.all()
    data = {'movies' : list(movies.values())} 
    
    return JsonResponse(data)


def movie_details(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    data = {
        'Movie_id': movie.id,
        'name': movie.name,
        'description': movie.description,
        'active': movie.active
    }
    return JsonResponse(data)