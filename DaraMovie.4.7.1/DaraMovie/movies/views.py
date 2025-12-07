from django.shortcuts import render, get_object_or_404
from .models import Movie, Genre
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


# Genre template view: each genre page and its movies in a list: 
# 1) sending the slug to render the template
# 2) passing the movies with the same genre to the template
def genre_detail_view(request,slug):
    genre = get_object_or_404(Genre,slug = slug)
    movies = Movie.objects.filter(genre = genre)
    context = {'genre':genre, 'movies':movies}
    return render(request,'movies/genre_detail.html',context)

# all genres 
def genre_list_view(request):
    all_genres = Genre.objects.all()
    context = {'genres':all_genres}
    return render (request,'movies/genre_list.html',context)
    