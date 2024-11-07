import re
from rest_framework import permissions

class GenrePermissionsClass(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.method == 'GET':
            
            # padrão: [nome da app].view_[nome do model]
            return request.user.has_permission('genres.view_genre')
        
        return False
    