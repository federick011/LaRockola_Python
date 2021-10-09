
from rest_framework import views, viewsets
from Servicios.serializers import *
from Servicios.permissions import *
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework.status import HTTP_400_BAD_REQUEST
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout

# Create your views here. Logica del Bakc end
"""class UsuarioAPI(viewsets.ModelViewSet):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated, AccesoPerfil)
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()"""

class ArtistSeriAPI(viewsets.ModelViewSet):
    serializer_class = ArtistSerializer
    queryset = Musico.objects.all()

class GenderSeriAPI(viewsets.ModelViewSet):
    serializer_class = GenderSerializer
    queryset = GeneroMusical.objects.all()

class AlbumSeriAPI(viewsets.ModelViewSet):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()

class SongsSeriAPI(viewsets.ModelViewSet):
    serializer_class = SongsSerializer
    queryset = Canciones.objects.all()

class PlayListAPI(viewsets.ModelViewSet):
    serializer_class = PlayListSerializer
    queryset = Playlist.objects.all()

#def Prueba(request):
    #Info del usuario
 #   return HttpResponse("Prueba de la seccion 'Servicios'")