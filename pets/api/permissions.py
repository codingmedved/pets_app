from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        user = request.user
        if obj.user == user or user.is_superuser:
            return True
        else:
            return False