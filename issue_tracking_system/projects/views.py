from django.contrib.auth.decorators import login_required
from rest_framework.viewsets import ModelViewSet

from .models import Project, Contributor
from .serializers import ProjectSerializer, CreateProjectSerializer


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

    @login_required
    def update(self, request, id):
        pass
