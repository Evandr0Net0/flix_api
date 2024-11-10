from rest_framework import permissions


class GlobalDefaultPermissions(permissions.BasePermission):
    
    def has_permission(self, request, view):
        model_permission_codename = self.__get_model_permission_codename(
            request.method,
            view=view,
        )
        
        if not model_permission_codename:
            return False
        
        return request.user.has_perm(model_permission_codename)
    
    def __get_model_permission_codename(self, method, view):
        try:
            # Buscando o nome do model
            model_name = view.queryset.model._meta.model_name
            # Buscando o nome da app
            app_label = view.queryset.model._meta.app_label
            # Buscando o tipo da action
            action = self.__get_action_sufix(method)
            return f'{app_label}.{action}_{model_name}'
        
        except AttributeError:
            return None
            
            
    # função para identificar os métodos e suas views
    def __get_action_sufix(self, method):
        method_actions = {
            'GET': 'view',
            'POST': 'add',
            'PUT': 'change',
            'PATCH': 'change',
            'DELETE': 'delete',
            'OPTIONS': 'view',
            'HEAD': 'view',
        }
        
        return method_actions.get(method, '')