from django.shortcuts import render, get_object_or_404
from .models import Movie

# Create your views here.


# get the movies from models.py and pass it to html to show 
def all_movie_view(request):
    movies = Movie.objects.all()
    context = {'movies':movies}
    return render (request,'movies/movie_all.html',context)

# movie deteil and slug: the slug going to be used in urls.py 
def movie_detail(request,slug):
    movie = get_object_or_404(Movie,slug=slug)
    context = {'movie':movie}
    return render(request,'movies/movie_detail',context)
    
