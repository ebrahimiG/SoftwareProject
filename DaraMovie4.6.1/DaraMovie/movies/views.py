from django.shortcuts import render, get_object_or_404
from .models import Movie
# Create your views here.

# a table for showing all movies
def all_movie_view(request):
    movies = Movie.objects.all()
    context = {'movies':movies}
    return render(request,'movies/movie_all.html',context)

# movie detail: 
# getting the slug from <a href="{% url "movie_detial" movie.slug %}"> in home page. with this function, we get the info from database about that movie with same the slug and sending the info to movie detail page while rendering it.
def movie_detail_view(request,slug):
    movie = get_object_or_404(Movie,slug= slug)
    context = {'movie':movie}
    return render (request,'movies/movie_detail.html',context)


