from rest_framework import permissions
from rest_framework.permissions import BasePermission

class AccesoPerfil (permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_anonymous:
            return False
        elif request.user.is_superuser:
            return True
        else:
            return request.user.username == obj.username

        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id