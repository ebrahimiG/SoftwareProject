from django.urls import path
from . import views

urlpatterns = [
    path('all-movies/',views.all_movie_view,name='all_movies'),
    path('movie-detail/<slug:slug>/',views.movie_detail_view,name='movie_detail'),
    path('genre/<slug:slug>/',views.genre_detail_view,name='genre_detail'),
    path('genre-list',views.genre_list_view,name='genre_list'),
]
