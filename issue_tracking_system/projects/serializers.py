from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Project, Contributor, Issue, Comment


class ProjectSerializer(ModelSerializer):

    issues = serializers.SerializerMethodField()
    contributors = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ['title', 'description', 'type', 'issues', 'contributors']

    def get_issues(self, instance):

        queryset = instance.issues.filter(project=Project)

        serializer = IssueSerializer(queryset, many=True)

        return serializer.data

    def get_contributors(self, instance):

        queryset = instance.contributors.filter(project=Project)

        serializer = ContributorSerializer(queryset, many=True)

        return serializer.data


class ContributorSerializer(ModelSerializer):

    class Meta:
        model = Contributor
        fields = ['user', 'project', 'role']


class IssueSerializer(ModelSerializer):

    comments = serializers.SerializerMethodField()

    class Meta:
        model = Issue
        fields = ['title', 'description', 'tag', 'priority', 'project', 'status', 'assignee', 'comments']

    def get_comments(self, instance):

        queryset = instance.comments.filter(issue=Issue)

        serializer = CommentSerializer(queryset, many=True)

        return serializer.data


class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = ['description']
