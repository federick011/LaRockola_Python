from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from django.contrib.auth.models import User, Group
from Servicios.models import *
from django.contrib.auth import get_user_model

class ArtistSerializer(serializers.ModelSerializer):
    class Meta():
        model = Musico
        fields = "__all__"

class GenderSerializer(serializers.ModelSerializer):
    class Meta():
        model = GeneroMusical
        fields = "__all__"

class AlbumSerializer(serializers.ModelSerializer):
    class Meta():
        model = Album
        fields = "__all__"

class SongsSerializer(serializers.ModelSerializer):
    class Meta():
        model = Canciones
        fields = "__all__"

class PlayListSerializer(serializers.ModelSerializer):
    class Meta():
        model = Playlist
        fields = "__all__"




