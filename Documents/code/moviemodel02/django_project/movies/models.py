from django.db import models

# Create your models here.

# Genre 
class Genre(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

# Country
class Country(models.Model):
    name = models.CharField(max_length=40)
    
    def __str__(self):
        return self.name
    
# Platform
class Platform(models.Model):
    name = models.CharField(max_length=40)
    
    def __str__(self):
        return self.name


# the movie model:
# title - poster - id - director -  actors - production year
#  - country/studio - genre(tags) - summery - rate - similar movies
class Movie(models.Model):
    title = models.CharField(max_length=70)
    poster = models.ImageField(upload_to='static/posters/')
    director = models.CharField(max_length=70)
    actors = models.TextField()
    release_date = models.DateField()
    summary = models.TextField()
    rate = models.FloatField()
    # (symmetrical = False) meaning if A is similar to B, B is not automatically similar to A
    similar_movies = models.ManyToManyField('self',blank=True,symmetrical=False)
    country = models.ManyToManyField(Country)
    platform = models.ManyToManyField(Platform)
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title
    
# country and company should be like Genre???