from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import BasePermission, SAFE_METHODS

from .models import Project, Contributor


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
        if view.action not in ("create", "update", "destroy"):
            return True

        return self.is_author(content_type=Project, pk=view.kwargs["project__pk"], user=request.user)


class IsContributorOfProject(BasePermission):

    def is_already_contributor_of_project(self, content_type, user, project):
        content = content_type.objects.filter(user=user, project=project).exists()
        if content is True:
            return False
        else:
            return True


class ContributorAlreadyExists(IsContributorOfProject):
    message = "You cannot add the same contributor twice."

    def has_permission(self, request, view):
        if view.action in ("create",):
            return self.is_already_contributor_of_project(content_type=Contributor, user=request.data["user"],
                                                          project=view.kwargs["project__pk"])


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
