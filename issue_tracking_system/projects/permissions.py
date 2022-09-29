from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import BasePermission, SAFE_METHODS

from .models import Contributor, Project


class IsAuthorOfProject(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            return obj.author == request.user


class IsContributorOfProject(BasePermission):

    def has_permission(self, request, view):
        contributors = Contributor.objects.filter(user=request.user).exists()
        return not contributors


class IsAuthorOfIssue(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            return obj.author == request.user


class IsAuthorOfComment(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            return obj.author == request.user
