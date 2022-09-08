from django.contrib.auth.decorators import login_required
from rest_framework.viewsets import ModelViewSet

from .models import Project, Contributor, Issue, Comment
from .serializers import ProjectSerializer, CreateProjectSerializer, UpdateProjectSerializer, DeleteProjectSerializer, \
    AddContributorSerializer, ContributorSerializer, DeleteContributorSerializer, IssueSerializer, \
    CreateIssueSerializer, UpdateIssueSerializer, DeleteIssueSerializer, CreateCommentSerializer, CommentSerializer, \
    UpdateCommentSerializer


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


class DeleteContributorViewSet(ModelViewSet):

    serializer_class = DeleteContributorSerializer

    @login_required
    def get_queryset(self, id):
        project = Project.objects.get(id=id)
        return Contributor.objects.filter(project=project)


class ListIssueViewSet(ModelViewSet):

    serializer_class = IssueSerializer

    @login_required
    def get_queryset(self, id):
        project = Project.objects.get(id=id)
        issues = Issue.objects.filter(project=project)
        return issues


class CreateIssueViewSet(ModelViewSet):

    serializer_class = CreateIssueSerializer

    @login_required
    def get_queryset(self, id):
        project = Project.objects.get(id=id)
        issues = Issue.objects.filter(project=project)
        return issues


class UpdateIssueViewSet(ModelViewSet):

    serializer_class = UpdateIssueSerializer

    @login_required
    def get_object(self, id):
        return Issue.objects.get(id=id)


class DeleteIssueViewSet(ModelViewSet):

    serializer_class = DeleteIssueSerializer

    @login_required
    def get_queryset(self, id):
        project = Project.objects.get(id=id)
        issues = Issue.objects.filter(project=project)
        return issues


class CreateCommentViewSet(ModelViewSet):

    serializer_class = CreateCommentSerializer

    @login_required
    def get_queryset(self, id):
        issue = Issue.objects.get(id=id)
        comments = Comment.objects.filter(issue=issue)
        return comments


class ListCommentViewSet(ModelViewSet):

    serializer_class = CommentSerializer

    @login_required
    def get_queryset(self, id):
        issue = Issue.objects.get(id=id)
        comments = Comment.objects.filter(issue=issue)
        return comments


class UpdateCommentViewSet(ModelViewSet):

    serializer_class = UpdateCommentSerializer

    @login_required
    def get_object(self, id):
        return Comment.object.get(id=id)
