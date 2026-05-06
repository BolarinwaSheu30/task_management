from rest_framework.permissions import BasePermission   # Base class for custom permissions

class IsOwner(BasePermission):
    """
    Custom permission:
    Only the owner of a task can access/modify it.
    """

    def has_object_permission(self, request, view, obj):
        """
        This runs when accessing a specific object (retrieve, update, delete)
        """
        return obj.owner == request.user   # Allow only if user owns the task