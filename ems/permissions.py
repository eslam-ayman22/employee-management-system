from rest_framework import permissions

class HasPermission(permissions.BasePermission):
    """
    Custom permission to check if the user has the required codename
    """

    def has_permission(self, request, view):
        
        required_permission = getattr(view, 'required_permission', None)

        if not required_permission:
            return True 

        user = request.user
        if not user.is_authenticated:
            return False

        user_permissions = user.get_all_permissions()  
        return required_permission in user_permissions
