from rest_framework import permissions

class GenrePermissionsClass(permissions.BasePermission):
    
    def has_permission(self, request, view):
        return True