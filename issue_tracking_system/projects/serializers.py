from rest_framework.serializers import ModelSerializer
from .models import Project, Contributor, Issue, Comment


class ProjectSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = ['title', 'description', 'type', 'author']


class ContributorSerializer(ModelSerializer):

    class Meta:
        model = Contributor
        fields = ['user', 'project', 'role']


class IssueSerializer(ModelSerializer):

    class Meta:
        model = Issue
        fields = ['title', 'description', 'tag', 'priority', 'project', 'status', 'author', 'assignee']


class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = ['description', 'author', 'issue']
