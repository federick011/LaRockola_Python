from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Usuarios.views import *
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register('usuarios', UserSeriAPI)
router.register('perfiles', ProfileAPI)

urlpatterns = [
    #path('ejemplo', Prueba)
    path('crud/', include(router.urls)),
    path('register', RegisterAPI.as_view()),
    path('login', LoginAPI.as_view()),
    path('logout', LogoutAPI.as_view()),
    #path('', views.feed, name='feed'),
    #path('profile/', views.profile, name = 'profile')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)