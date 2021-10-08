
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

class ProfileAPI (viewsets.ModelViewSet):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated, AccesoPerfil)
    serializer_class = ProfileSerializer
    queryset = Perfil.objects.all()

class UserSeriAPI(viewsets.ModelViewSet):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated, AccesoPerfil)
    serializer_class = UserSerializer
    queryset = User.objects.all()


class SongsSeriAPI(viewsets.ModelViewSet):
    serializer_class = SongsSerializer
    queryset = Canciones.objects.all()

class GenderSeriAPI(viewsets.ModelViewSet):
    serializer_class = GenderSerializer
    queryset = GeneroMusical.objects.all()

class RegisterAPI(views.APIView):
    def post(self, request):
        usuario = UserSerializer(data=request.data)
        if usuario.is_valid():
            #¿Información válida?
            usuario.save()
            return Response({"Bienvenido": True})
        return Response(usuario.errors, HTTP_400_BAD_REQUEST)

class LoginAPI(views.APIView):
    def post(self, request):
        usuario = authenticate(request, username=request.data['username'], password = request.data['password'])
        if not usuario is None:
            login(request, usuario)
            return Response({"Bienvenido": True})
        return Response({"Bienvenido": False})

class LogoutAPI(views.APIView):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated, AccesoPerfil)
    def get(self, request):
        logout(request)
        return Response({"Adiós":True})

#def Prueba(request):
    #Info del usuario
 #   return HttpResponse("Prueba de la seccion 'Servicios'")