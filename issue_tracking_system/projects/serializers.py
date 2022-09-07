from rest_framework.serializers import ModelSerializer
from .models import Project, Contributor, Issue, Comment


class ProjectSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = ['title', 'description', 'type']


class ContributorSerializer(ModelSerializer):

    class Meta:
        model = Contributor
        fields = ['project', 'role']


class IssueSerializer(ModelSerializer):

    class Meta:
        model = Issue
        fields = ['title', 'description', 'tag', 'priority', 'project', 'status', 'assignee']


class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = ['description']
