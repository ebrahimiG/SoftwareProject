from django.shortcuts import render
from .models import Movie
# Create your views here.

def all_movie_view(request):
    movies = Movie.objects.all()
    context = {'movies':movies}
    return render(request,'movies/movie_all.html',context)
