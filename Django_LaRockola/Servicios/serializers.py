from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from django.contrib.auth.models import User, Group
from Servicios.models import *
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = ["username", "password", "email"]
        extra_kwargs = {
            'password':{'write_only':True}, 
            "style":{'input_type': 'password'}
            }

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta():
        model = Perfil
        fields = "__all__"
        

class GenderSerializer(serializers.ModelSerializer):
    class Meta():
        model = GeneroMusical
        fields = "__all__"

class SongsSerializer(serializers.ModelSerializer):
    class Meta():
        model = Canciones
        fields = "__all__"






