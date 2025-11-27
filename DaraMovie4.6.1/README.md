# DaraMovie 4.6.1
first of all make sure to install django, pillow and ollama in venv
imporvment in the structure of the project <br>
adding __featured section__ class so the movies can be in different sections like top ten, batman collection or ...

## step 1: 
create the movie model and some object from it. around 20 is good. --> i made 11 <br>
then try to show those movies with the __FeaturedSection__ class in the home page. <br>
i showed the movies in home page using this in views.py : 
```
# home page
def home_view(request):
    # select four movies from database (usually starts from the oldest movie object)
    topten_sec = Movie.objects.all()[:4]
    # select the four movie that recently created ('-id')
    blog_sec = Movie.objects.order_by('-id')[:4]

    context = {
        'topten':topten_sec,
        'blog':blog_sec
    }
    return render(request,'main/home.html',context)
```

## step 2: 
go for filmyar and make sure it's working. everythig is working so far.

## step 3: 
go for the movies app and create __movies_all.html__, __movie_detail.html__, __genre_index.html__ and __genre_page.html__.<br>
create some genres and work with them. <br>
* movies_all.html ✅
* movie_detail.html



