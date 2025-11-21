from django.urls import path
from . import views

urlpatterns = [
    path('all/',views.all_movie_view,name='all_movies'),
    path('<slug:slug>/',views.movie_detail,name='movie_detail'),
]
