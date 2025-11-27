from django.urls import path
from . import views

urlpatterns = [
    path('all-movies/',views.all_movie_view,name='all_movies'),
]
