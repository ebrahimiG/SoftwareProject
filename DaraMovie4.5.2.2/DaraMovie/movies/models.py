from django.db import models
from django.utils.text import slugify

# Create your models here.

# Genre
class Genre(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

# Country
class Country(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

# Platform
class Platform(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


# the movie model:
# maybe make everything like Genre, It's good for the advanced search but in this project keep it simple
# title - poster - id - director -  actors - production year
#  - country/studio - genre(tags) - summery - rate - similar movies
class Movie(models.Model):
    title = models.CharField(max_length=70)
    # slug is for to be more user and SEO friendly
    slug = models.SlugField(unique=True, blank=True)
    poster = models.ImageField(blank=True,upload_to='static/Uploaded_posters/')
    director = models.CharField(max_length=70)
    actors = models.TextField()
    release_date = models.DateField()
    country = models.ManyToManyField(Country,blank=True)
    platform = models.ManyToManyField(Platform,blank=True)
    genres = models.ManyToManyField(Genre)
    summary = models.TextField()
    # i don't know what decimalfield does
    rate = models.DecimalField(max_digits=3, decimal_places=1)
    similar_movies = models.ManyToManyField('self', blank=True)

    # Ensures every movie automatically gets a slug when saved and Lets you still override the slug manually if needed.
    # Uses Django’s slugify function to convert the movie title into a URL‑friendly string.
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    # showing the title in admin panel table
    def __str__(self):
        return self.title
