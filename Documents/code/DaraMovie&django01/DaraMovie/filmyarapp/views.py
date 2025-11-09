from django.shortcuts import render

# Create your views here.
def filmyar_view(request):
    return render(request,'filmyarapp/filmyar.html')