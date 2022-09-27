from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import BasePermission, SAFE_METHODS

from .models import Project, Contributor, Issue, Comment


class IsAuthorOfProject(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            return obj.author == request.user


class IsContributorOfProject(BasePermission):

    def has_object_permission(self, request, view, obj):
        obj = Contributor.objects.filter(user=request.user).values('project')
        return bool(request.user and request.user.is_authenticated and obj)


class IsAuthorOfIssue(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            return obj.author == request.user


class IsAuthorOfComment(BasePermission):

    def has_object_permission(self, request, view, obj):
        obj = Comment.objects.get(author=request.user)
        return bool(request.user and request.user.is_authenticated and obj)
