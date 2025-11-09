from django.urls import path
from . import views

urlpatterns = [
    path('',views.filmyar_view,name='filmyar'),
]
