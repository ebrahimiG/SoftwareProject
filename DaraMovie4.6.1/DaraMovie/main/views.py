from django.shortcuts import render
from movies.models import Movie 



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


# about us page
def about_view(request):
    return render(request,'main/about.html')


# contact us page
def contact_view(request):
    return render(request,'main/contact.html')


# faq page
def faq_view(request):
    return render(request,'main/faq.html')


#  page
def subs_view(request):
    return render(request,'main/subs.html')