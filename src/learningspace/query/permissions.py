from django.contrib.auth.models import Group
from rest_framework import permissions


class IsStudent(permissions.BasePermission):
    """
    permission for admins
    """

    def has_permission(self, request, view):
        return bool(request.user.is_student and request.user.is_authenticated)

class IsMentor(permissions.BasePermission):
    """
    permission for admins
    """

    def has_permission(self, request, view):
        return bool(request.user.is_mentor and request.user.is_authenticated)
