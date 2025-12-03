from django.urls import path
from . import views
urlpatterns = [
    path('',views.home_view,name='home'),
    path('about/',views.about_view,name='about'),
    path('contact/',views.contact_view,name='contact'),
    path('faq/',views.faq_view,name='faq'),
    path('subscription/',views.subs_view,name='sub'),
]
