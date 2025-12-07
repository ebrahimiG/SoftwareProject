from django.db import models
from django.utils.text import slugify

# Create your models here.

# Genre class: adding slug field
class Genre(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

# Country class
class Country(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

# Platform class
class Platform(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

# People class for directors and actors
class People(models.Model):
    name = models.CharField(max_length=30)
    role_list = [
        ('Director','Director'),
        ('Actor','Actor'),
    ]
    role = models.CharField(max_length=10,choices=role_list)
    def __str__(self):
        return self.name
    
# Movie class: 
class Movie(models.Model):
    title = models.CharField(max_length=100)
    director = models.ManyToManyField(People,limit_choices_to={'role':'Director'},related_name='directed_movies')
    actors = models.ManyToManyField(People,limit_choices_to={'role':'Actor'},related_name='acted_movies',blank=True)
    poster = models.ImageField(upload_to='posters/')
    summary = models.TextField()
    rate = models.DecimalField(max_digits=3, decimal_places=1)
    release_date = models.DateField()
    country = models.ManyToManyField(Country,blank=True)
    platform = models.ManyToManyField(Platform,blank=True)
    similar_movies = models.ManyToManyField('self',blank=True,symmetrical=False)
    genre = models.ManyToManyField(Genre)
    slug = models.SlugField(unique=True, blank=True)

    # Ensures every movie automatically gets a slug when saved and Lets you still override the slug manually if needed.
    # Uses Django’s slugify function to convert the movie title into a URL‑friendly string.
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    

# Serise class if needed...
"""class Serise(models.Model):
    title = models.CharField(max_length=100)
    director = models.ManyToManyField(People,limit_choices_to={'role':'Director'},related_name='directed_movies')
    actors = models.ManyToManyField(People,limit_choices_to={'role':'Actor'},related_name='acted_movies',blank=True)
    poster = models.ImageField(upload_to='static/posters')
    summary = models.TextField()
    rate = models.DecimalField(max_digits=3, decimal_places=1)
    release_year = models.DateField()
    country = models.ManyToManyField(Country,blank=True)
    platform = models.ManyToManyField(Platform,blank=True)
    similar_movies = models.ManyToManyField('self',blank=True,symmetrical=False) 
    genre = models.ManyToManyField(Genre)
    slug = models.SlugField(unique=True, blank=True)

    stats_list = [
       ('Ongoing','Ongoing'),
       ('Finished','Finished'),
       ('Canceld','Canceld'),
       ('Unspecified','Unspecified'),
   ]
    stats = models.CharField(max_length = 30,choises = stats_list)
    number_of_seasons = models.IntegerField()
    number_of_episodes = models.IntegerField()

    # Ensures every movie automatically gets a slug when saved and Lets you still override the slug manually if needed.
    # Uses Django’s slugify function to convert the movie title into a URL‑friendly string.
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title"""
    


# Section Tag class for collections, top 10 and ... 
# most likely to use in home page
# it uses Movie class to gather movies in a collection.
class SectionTag(models.Model):
    section_name = models.CharField(max_length=70)
    movies = models.ManyToManyField(Movie,blank=True)
    slug = models.SlugField(unique=True,blank=True)
    order = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.section_name
