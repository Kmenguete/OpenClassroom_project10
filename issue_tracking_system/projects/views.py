# from django.db.models import Q
from itertools import chain

from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from . import models
from .models import Project, Contributor, Issue, Comment
from .serializers import ProjectListSerializer, ContributorSerializer, IssueSerializer, CommentSerializer, \
    ProjectDetailSerializer


class ProjectViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post", "put", "delete"]
    serializer_class = ProjectListSerializer

    def get_queryset(self):
        queryset = Project.objects.filter(author=self.request.user)
        projects_as_contributor = Contributor.objects.filter(user=self.request.user).values('project')
        queryset_2 = include_projects_as_contributor(projects_as_contributor)
        real_queryset = list(chain(queryset, queryset_2))
        print("Here this is the real queryset:" + str(real_queryset))
        new_queryset = convert_list_to_queryset(real_queryset)
        project_id = self.request.GET.get('project_id')
        if project_id is not None:
            new_queryset.filter(id=project_id)
        return new_queryset

    def create(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data["author"] = request.user.pk
        request.POST._mutable = False
        return super(ProjectViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data["author"] = request.user.pk
        request.POST._mutable = False
        return super(ProjectViewSet, self).update(request, *args, **kwargs)


def include_projects_as_contributor(projects_as_contributor):
    projects_to_include = [projects_as_contributor]
    for project in projects_to_include:
        projects = Project.objects.filter(id__in=project)
        return projects


def convert_list_to_queryset(real_queryset):
    for project in real_queryset:
        projects = Project.objects.filter(id__in=project)
        return projects


class DetailProjectViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post", "put", "delete"]
    serializer_class = ProjectDetailSerializer

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj


class ContributorViewSet(ModelViewSet):
    serializer_class = ContributorSerializer
    http_method_names = ["get", "post", "delete"]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Contributor.objects.all()
        project_id = self.request.GET.get('project_id')
        if project_id is not None:
            queryset = queryset.filter(id=project_id)
        return queryset

    def create(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data["permission"] = True
        request.POST._mutable = False
        return super(ContributorViewSet, self).create(request, *args, **kwargs)


class IssueViewSet(ModelViewSet):
    serializer_class = IssueSerializer
    http_method_names = ["get", "post", "put", "delete"]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Issue.objects.all()
        project_id = self.request.GET.get('project_id')
        if project_id is not None:
            queryset = queryset.filter(id=project_id)
        return queryset

    def create(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data["author"] = request.user.pk
        request.POST._mutable = False
        return super(IssueViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(IssueViewSet, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(IssueViewSet, self).destroy(request, *args, **kwargs)


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    http_method_names = ["get", "post", "put", "delete"]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Comment.objects.all()
        issue_id = self.request.GET.get('issue_id')
        if issue_id is not None:
            queryset = queryset.filter(id=issue_id)
        return queryset

    def create(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data["author"] = request.user.pk
        request.POST._mutable = False
        return super(CommentViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(CommentViewSet, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(CommentViewSet, self).destroy(request, *args, **kwargs)
