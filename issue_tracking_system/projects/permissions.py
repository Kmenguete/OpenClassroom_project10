from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import BasePermission, SAFE_METHODS

from .models import Contributor, Project


class IsAuthorOfProject(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            return obj.author == request.user


class IsAuthor(BasePermission):
    def is_author(self, content_type, pk, user):
        try:
            content = content_type.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return True

        return content.author == user


class IsProjectAuthorFromProjectView(IsAuthor):
    def has_permission(self, request, view):
        project = get_object_or_404(Project, id=view.kwargs['pk'])
        if view.action not in ("create", "update", "destroy"):
            return True

        return self.is_author(content_type=project, pk=view.kwargs["pk"], user=request.user)


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
