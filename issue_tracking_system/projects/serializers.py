from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Project, Contributor, Issue, Comment


class ProjectDetailSerializer(ModelSerializer):

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


class ProjectListSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = ['title', 'description', 'type', 'author']


class ContributorSerializer(ModelSerializer):

    class Meta:
        model = Contributor
        fields = ['user', 'project', 'role']
        depth = 1


class IssueSerializer(ModelSerializer):

    class Meta:
        model = Issue
        fields = ['title', 'description', 'tag', 'priority', 'project', 'status', 'author', 'assignee']


class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = ['description', 'author', 'issue']
