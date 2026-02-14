from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __clstr__(self):
        return self.name

class Stage(models.Model):
    project = models.ForeignKey(Project, related_name='stages', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.project.name} - {self.name}"

class Task(models.Model):
    stage = models.ForeignKey(Stage, related_name='tasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    assigned_to = models.ForeignKey(User, related_name='tasks', on_delete=models.SET_NULL, null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    task = models.ForeignKey(Task, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)