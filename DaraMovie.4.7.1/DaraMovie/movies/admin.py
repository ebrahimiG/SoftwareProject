from django.contrib import admin
from .models import Genre,Movie,Platform,People,SectionTag,Country

# Register your models here.

admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(People)
admin.site.register(Platform)
admin.site.register(Country)
admin.site.register(SectionTag)

