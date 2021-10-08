from django.db import models
from django.db.models.fields import CharField
from datetime import datetime
from django.utils.timezone import *

# Create your models here. Cone

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
    Avatar = models.ImageField(null = True, blank = True)
    IsMusician = models.BooleanField(default=False)
    
    def __str__(self):
        return self.Name

class GeneroMusical(models.Model):
    GenderName = models.CharField(max_length=200, null= True, blank= True)

    def __str__(self):
        return self.GenderName

class Canciones(models.Model):
    Artist = models.ForeignKey(User, on_delete=models.CASCADE)
    GenderSong = models.ForeignKey(GeneroMusical, default="0", on_delete=models.CASCADE)
    SongName = models.CharField(max_length=200, default="Unknow" , null = True, blank = True)
    AvatarSong = models.ImageField(null = True, blank = True)
    Views = models.IntegerField(default=0, null = True, blank = True)

    #Agregarmos vistas cada que se abra la cancion
    def AddViews(self):
        self.Views+=1
        self.save()

    def __str__(self):
        return self.SongName

    





