from django.contrib.auth.decorators import login_required
from rest_framework.viewsets import ModelViewSet

from .models import Project, Contributor
from .serializers import ProjectSerializer


class ProjectViewSet(ModelViewSet):

    serializer_class = ProjectSerializer

    @login_required
    def get_queryset(self, request):
        return Project.objects.filter(author=request.user), \
               Contributor.objects.filter(user=request.user).values('project')
