from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# creatin a Chat model to store and show user chat history:

class Chat(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)