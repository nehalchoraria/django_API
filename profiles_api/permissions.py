from rest_framework import permissions

class update_on_profile(permissions.BasePermission):
    '''Allow user to only edit own profile'''

    def has_object_permission(self, request, view, obj):
        '''Check if user is trying to edit own profile'''
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id