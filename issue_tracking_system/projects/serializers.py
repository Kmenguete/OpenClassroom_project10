from django.contrib.auth.decorators import login_required
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


class CreateProjectSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = ('title', 'description', 'type')

    @login_required
    def create(self, validated_data, request):
        project = Project.objects.create(
            title=validated_data['title'],
            description=validated_data['description'],
            type=validated_data['type']
        )
        project.author = request.user
        project.save()

        return project


class UpdateProjectSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = ('title', 'description', 'type')

    @login_required
    def update(self, id, validated_data):
        project = Project.objects.get(id=id).update(
            title=validated_data['title'],
            description=validated_data['description'],
            type=validated_data['type']
        )

        project.save()

        return project


class DeleteProjectSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = ('title', 'description', 'type')

    @login_required
    def __delete__(self, id):
        project = Project.objects.get(id=id)
        project.delete()


class ContributorSerializer(ModelSerializer):

    class Meta:
        model = Contributor
        fields = ['user', 'project', 'role']


class AddContributorSerializer(ModelSerializer):

    class Meta:
        model = Contributor
        fields = ('user', 'project', 'role')

    @login_required
    def create(self, validated_data):
        contributor = Contributor.objects.create(
            user=validated_data['user'],
            project=validated_data['project'],
            role=validated_data['role']
        )

        contributor.save()

        return contributor


class DeleteContributorSerializer(ModelSerializer):

    class Meta:
        model = Contributor
        fields = ('user', 'project', 'role')

    @login_required
    def __delete__(self, id):
        contributor = Contributor.objects.get(id=id)
        contributor.delete()


class IssueSerializer(ModelSerializer):

    comments = serializers.SerializerMethodField()

    class Meta:
        model = Issue
        fields = ['title', 'description', 'tag', 'priority', 'project', 'status', 'assignee', 'comments']

    def get_comments(self, instance):

        queryset = instance.comments.filter(issue=Issue)

        serializer = CommentSerializer(queryset, many=True)

        return serializer.data


class CreateIssueSerializer(ModelSerializer):

    class Meta:
        model = Issue
        fields = ('title', 'description', 'tag', 'priority', 'project', 'status', 'assignee')

    @login_required
    def create(self, validated_data):
        issue = Issue.objects.create(
            title=validated_data['title'],
            description=validated_data['description'],
            tag=validated_data['tag'],
            priority=validated_data['priority'],
            project=validated_data['project'],
            status=validated_data['status'],
            assignee=validated_data['assignee']
        )

        issue.save()

        return issue


class UpdateIssueSerializer(ModelSerializer):

    class Meta:
        model = Issue
        fields = ('title', 'description', 'tag', 'priority', 'project', 'status', 'assignee')

    @login_required
    def update(self, id, validated_data):
        issue = Issue.objects.get(id=id).update(
            title=validated_data['title'],
            description=validated_data['description'],
            tag=validated_data['tag'],
            priority=validated_data['priority'],
            project=validated_data['project'],
            status=validated_data['status'],
            assignee=validated_data['assignee']
        )

        issue.save()

        return issue


class DeleteIssueSerializer(ModelSerializer):

    class Meta:
        model = Issue
        fields = ('title', 'description', 'tag', 'priority', 'project', 'status', 'assignee')

    @login_required
    def __delete__(self, id):
        issue = Issue.objects.get(id=id)
        issue.delete()


class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = ['description']


class CreateCommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = ('description', )

    @login_required
    def create(self, validated_data):
        comment = Comment.objects.create(
            description=validated_data['description']
        )

        comment.save()

        return comment


class UpdateCommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = ('description', )

    @login_required
    def update(self, id, validated_data):
        comment = Comment.objects.get(id=id).update(
            description=validated_data['description']
        )

        comment.save()

        return comment


class DeleteCommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = ('description', )

    @login_required
    def __delete__(self, id):
        comment = Comment.objects.get(id=id)
        comment.delete()
