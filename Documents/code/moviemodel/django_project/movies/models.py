from django.db import models

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=70)
    genres = models.ManyToManyField(Genre)
    # test to see where the posters go...
    poster = models.ImageField(upload_to='posters/')
    director = models.CharField(max_length=70)
    production_year = models.DateField()
    actors = models.TextField()
    country_company = models.CharField(max_length=70)
    summery = models.TextField()
    rate = models.FloatField()

    def __str__(self):
        return self.title