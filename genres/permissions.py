from django.template.context_processors import request
from rest_framework import permissions

class GenrePermissionsClass(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.method == 'GET':
            # padrão: [nome da app].view_[nome do model]
            return request.user.has_perm('genres.view_genre')
        if request.method == 'POST':
            return request.user.has_perm('genres.add_genre')
        
        if request.method in ['PATCH', 'PUT']:
            return request.user.has_perm('genres.change_genre')
        
        if request.method == 'DELETE':
            return request.user.has_perm('genres.delete_genre')
        
        return False
    