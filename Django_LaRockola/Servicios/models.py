from django.db import models
from django.db.models import base
from django.db.models.fields import CharField
from datetime import datetime
from django.utils.timezone import *

# Create your models here. Conexion base de datos

class Formato(models.Model):
    nombre = models.CharField(max_length=150,primary_key=True,default="Unknown")
    cantLikes = models.IntegerField(default=0)
    cantVistas = models.IntegerField(default=0)
    description = models.TextField(max_length=1000,default="",null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.nombre

    def addlike(self):
        self.cantLikes+=1
        self.save()

    def AddViews(self):
        self.cantVistas+=1
        self.save()

class Musico(Formato):
    nombreArtista = models.CharField(max_length=100, null= True, blank= True)
    apellidoArtista = models.CharField(max_length=100, null= True, blank= True)

class GeneroMusical(Formato):
    imagengenero = models.ImageField(null= True, blank=True)

class Album(Formato):
    generos = models.ManyToManyField(GeneroMusical)
    musico = models.ManyToManyField(Musico)
    caratula = models.ImageField(null= True, blank=True)

    def __str__(self):
        return self.nombre

class Canciones(Formato):
    artist = models.ManyToManyField(Musico, default="Unknown")
    albumArtista = models.ForeignKey(Album, default="0",on_delete=models.CASCADE)
    genderSong = models.ManyToManyField(GeneroMusical, default="0")
    avatarSong = models.ImageField(null = True, blank = True)
    song = models.FileField()
    duration = models.TimeField(null=True, blank= True)
    releaseDate = models.DateField(null= True, blank= True)

    #Agregarmos vistas cada que se abra la cancion

    def addlike(self):
        super().addlike

        generos = self.genderSong.all()
        for genero in generos:
            genero.addlike()
        
        musicos = self.musico_set.all()
        for musico in musicos:
            musico.addlike()

    def AddViews(self):
        super().AddViews

        generos = self.genderSong.all()
        for genero in generos:
            genero.addViews()
        
        musicos = self.musico_set.all()
        for musico in musicos:
            musico.addViews()
class Playlist(models.Model):
    list = (
        ("Antes 1960","Before 60's"),
        ("1960 - 1980","60's - 70's"),
        ("1980 - 2000","80's - 90's"),
        ("2000 - actualidad","2000's - 2020's"),
    )
    nombre_playlist = models.CharField(max_length=100, default="Unknown", choices = list)
    canciones = models.ManyToManyField(Canciones)
    musicos=  models.ManyToManyField(Musico)

    def __str__(self):
        return self.nombre_playlist

