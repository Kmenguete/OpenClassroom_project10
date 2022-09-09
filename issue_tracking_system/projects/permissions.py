from rest_framework.permissions import BasePermission

from .models import Project, Contributor, Issue, Comment


class IsAuthorOfProject(BasePermission):

    def has_object_permission(self, request, view, obj):
        obj = Project.objects.get(author=request.user)
        return bool(request.user and request.user.is_authenticated and obj)


class IsContributorOfProject(BasePermission):

    def has_object_permission(self, request, view, obj):
        obj = Contributor.objects.filter(user=request.user).values('project')
        return bool(request.user and request.user.is_authenticated and obj)


class IsAuthorOfIssue(BasePermission):

    def has_object_permission(self, request, view, obj):
        obj = Issue.objects.get(author=request.user)
        return bool(request.user and request.user.is_authenticated and obj)


class IsAuthorOfComment(BasePermission):

    def has_object_permission(self, request, view, obj):
        obj = Comment.objects.get(author=request.user)
        return bool(request.user and request.user.is_authenticated and obj)
