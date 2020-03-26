from rest_framework.permissions import BasePermission


class IsOwnerUser(BasePermission):
    """
    Allows access only for owner of the resource.
    """
    message = "You must be the owner of the resource."

    def has_object_permission(self, request, view, obj):
        return bool(request.user and (request.user.is_staff or request.user == obj))
