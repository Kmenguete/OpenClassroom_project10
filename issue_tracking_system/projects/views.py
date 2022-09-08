from django.contrib.auth.decorators import login_required
from rest_framework.viewsets import ModelViewSet

from .models import Project, Contributor
from .serializers import ProjectSerializer, CreateProjectSerializer, UpdateProjectSerializer, DeleteProjectSerializer, \
    AddContributorSerializer, ContributorSerializer


class ProjectViewSet(ModelViewSet):

    serializer_class = ProjectSerializer

    @login_required
    def get_queryset(self, request):
        return Project.objects.filter(author=request.user), \
               Contributor.objects.filter(user=request.user).values('project')


class CreateProjectViewSet(ModelViewSet):

    serializer_class = CreateProjectSerializer

    @login_required
    def get_queryset(self, request):
        return Project.objects.filter(author=request.user), \
               Contributor.objects.filter(user=request.user).values('project')


class DetailProjectViewSet(ModelViewSet):

    serializer_class = ProjectSerializer

    @login_required
    def get_object(self, id):
        return Project.objects.get(id=id)


class UpdateProjectViewSet(ModelViewSet):

    serializer_class = UpdateProjectSerializer

    @login_required
    def get_object(self, id):
        return Project.objects.get(id=id)


class DeleteProjectViewSet(ModelViewSet):

    serializer_class = DeleteProjectSerializer

    @login_required
    def get_queryset(self, request):
        return Project.objects.filter(author=request.user), \
               Contributor.objects.filter(user=request.user).values('project')


class AddContributorViewSet(ModelViewSet):

    serializer_class = AddContributorSerializer

    @login_required
    def get_queryset(self, id):
        project = Project.objects.get(id=id)
        return Contributor.objects.filter(project=project)


class ListContributorViewSet(ModelViewSet):

    serializer_class = ContributorSerializer

    @login_required
    def get_queryset(self, id):
        project = Project.objects.get(id=id)
        return Contributor.objects.filter(project=project)
