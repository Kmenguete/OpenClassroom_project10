from django.conf import settings
from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    type = models.CharField(max_length=128)
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None
    )

    def __str__(self):
        return self.title


class Contributor(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE, default="")
    permission = models.BooleanField(default=False, blank=True)
    role = models.CharField(max_length=128)

    def __str__(self):
        return self.role


class Issue(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    tag = models.CharField(max_length=128)
    priority = models.CharField(max_length=128)
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    status = models.CharField(max_length=128)
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="author",
        default=None,
    )
    assignee = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="assignee",
        default=None,
    )
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    description = models.CharField(max_length=256)
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None
    )
    issue = models.ForeignKey(to=Issue, on_delete=models.CASCADE, default=None)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description
