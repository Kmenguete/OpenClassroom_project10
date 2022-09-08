from django.contrib.auth.decorators import login_required
from rest_framework.serializers import ModelSerializer
from .models import Project, Contributor, Issue, Comment


class ProjectSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = ['title', 'description', 'type']


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


class IssueSerializer(ModelSerializer):

    class Meta:
        model = Issue
        fields = ['title', 'description', 'tag', 'priority', 'project', 'status', 'assignee']


class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = ['description']
