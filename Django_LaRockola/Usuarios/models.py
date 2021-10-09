from django.db import models
from django.contrib.auth.models import User
from django.db.models import base
from django.db.models.fields import CharField
from datetime import date, datetime, timezone
from django.utils.timezone import *

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200, null = True, blank = True)
    email = models.EmailField(null = True, blank = True)
    
    def __str__(self):
        return str(self.username)

class Perfil(models.Model):
    Name = models.ForeignKey(User, on_delete=models.CASCADE)
    LastName = models.CharField(max_length=200, null = True, blank = True)
    UserName = models.CharField(max_length=200, null = True, blank = True)
    BirthDay = models.DateField(null = True, blank = True)
    Avatar = models.ImageField(default='avatarusuario.png')
    IsMusician = models.BooleanField(default=False)

    def __str__(self):
        return str(self.Name)

class Post(models.Model):
    usuario = models.ForeignKey(User,on_delete=models.CASCADE, related_name = 'posts')
    tiempocomentario = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        ordering = ['-tiempocomentario']

    def __str__(self):
        return str(self.usuario.username) + ": " + str(self.content) + " at: " + str(self.tiempocomentario)