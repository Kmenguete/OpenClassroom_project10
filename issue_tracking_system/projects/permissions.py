from rest_framework.permissions import BasePermission

from .models import Project, Contributor


class IsAuthorOfProject(BasePermission):

    def has_object_permission(self, request, view, obj):
        obj = Project.objects.get(author=request.user)
        return bool(request.user and request.user.is_authenticated and obj)


class IsContributorOfProject(BasePermission):

    def has_object_permission(self, request, view, obj):
        obj = Contributor.objects.filter(user=request.user).values('project')
        return bool(request.user and request.user.is_authenticated and obj)
