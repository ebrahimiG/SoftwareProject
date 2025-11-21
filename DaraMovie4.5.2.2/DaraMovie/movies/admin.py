from django.contrib import admin
from .models import Genre, Country, Platform, Movie

# Register your models here.

admin.site.register(Genre)
admin.site.register(Country)
admin.site.register(Platform)
admin.site.register(Movie)
