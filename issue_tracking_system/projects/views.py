from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Project, Contributor, Issue, Comment
from .serializers import ProjectSerializer, CreateProjectSerializer, UpdateProjectSerializer, DeleteProjectSerializer, \
    AddContributorSerializer, ContributorSerializer, DeleteContributorSerializer, IssueSerializer, \
    CreateIssueSerializer, UpdateIssueSerializer, DeleteIssueSerializer, CreateCommentSerializer, CommentSerializer, \
    UpdateCommentSerializer, DeleteCommentSerializer


class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Project.objects.filter(author=user), Contributor.objects.filter(user=user).values('project')


class CreateProjectViewSet(ModelViewSet):
    serializer_class = CreateProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Project.objects.filter(author=user), Contributor.objects.filter(user=user).values('project')


class DetailProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Project.objects.all()
        project_id = self.request.GET.get('project_id')
        if project_id is not None:
            queryset = queryset.filter(id=project_id)
        return queryset


class UpdateProjectViewSet(ModelViewSet):
    serializer_class = UpdateProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Project.objects.all()
        project_id = self.request.GET.get('project_id')
        if project_id is not None:
            queryset = queryset.filter(id=project_id)
        return queryset


class DeleteProjectViewSet(ModelViewSet):
    serializer_class = DeleteProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Project.objects.filter(author=user), Contributor.objects.filter(user=user).values('project')


class AddContributorViewSet(ModelViewSet):
    serializer_class = AddContributorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Contributor.objects.all()
        project_id = self.request.GET.get('project_id')
        if project_id is not None:
            queryset = queryset.filter(id=project_id)
        return queryset


class ListContributorViewSet(ModelViewSet):
    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Contributor.objects.all()
        project_id = self.request.GET.get('project_id')
        if project_id is not None:
            queryset = queryset.filter(id=project_id)
        return queryset


class DeleteContributorViewSet(ModelViewSet):
    serializer_class = DeleteContributorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Contributor.objects.all()
        project_id = self.request.GET.get('project_id')
        if project_id is not None:
            queryset = queryset.filter(id=project_id)
        return queryset


class ListIssueViewSet(ModelViewSet):
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Issue.objects.all()
        project_id = self.request.GET.get('project_id')
        if project_id is not None:
            queryset = queryset.filter(id=project_id)
        return queryset


class CreateIssueViewSet(ModelViewSet):
    serializer_class = CreateIssueSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Issue.objects.all()
        project_id = self.request.GET.get('project_id')
        if project_id is not None:
            queryset = queryset.filter(id=project_id)
        return queryset


class UpdateIssueViewSet(ModelViewSet):
    serializer_class = UpdateIssueSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Issue.objects.all()
        project_id = self.request.GET.get('project_id')
        if project_id is not None:
            queryset = queryset.filter(id=project_id)
        return queryset


class DeleteIssueViewSet(ModelViewSet):
    serializer_class = DeleteIssueSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Issue.objects.all()
        project_id = self.request.GET.get('project_id')
        if project_id is not None:
            queryset = queryset.filter(id=project_id)
        return queryset


class CreateCommentViewSet(ModelViewSet):
    serializer_class = CreateCommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Comment.objects.all()
        issue_id = self.request.GET.get('issue_id')
        if issue_id is not None:
            queryset = queryset.filter(id=issue_id)
        return queryset


class ListCommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Comment.objects.all()
        issue_id = self.request.GET.get('issue_id')
        if issue_id is not None:
            queryset = queryset.filter(id=issue_id)
        return queryset


class UpdateCommentViewSet(ModelViewSet):
    serializer_class = UpdateCommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Comment.objects.all()
        issue_id = self.request.GET.get('issue_id')
        if issue_id is not None:
            queryset = queryset.filter(id=issue_id)
        return queryset


class DeleteCommentViewSet(ModelViewSet):
    serializer_class = DeleteCommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Comment.objects.all()
        issue_id = self.request.GET.get('issue_id')
        if issue_id is not None:
            queryset = queryset.filter(id=issue_id)
        return queryset


class DetailCommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Comment.objects.all()
        issue_id = self.request.GET.get('issue_id')
        if issue_id is not None:
            queryset = queryset.filter(id=issue_id)
        return queryset
