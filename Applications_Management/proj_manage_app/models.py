from django.db import models
from login_app.models import User

class ProjectManager(models.Manager):
  def basic_validator(self, postData):
    errors = {}
    if len(postData['title']) <= 5:
      errors['title'] = 'Title must be longer than 5 characters.'
    if len(postData['desc']) <= 10:
      errors['desc'] = 'Desc must be longer than 10 characters.'
    return errors;

class TaskManager(models.Manager):
  def basic_validator(self, postData):
    errors = {}
    if len(postData['title']) <= 5:
      errors['title'] = 'Title must be longer than 5 characters.'
    if len(postData['desc']) <= 10:
      errors['desc'] = 'Desc must be longer than 10 characters.'
    return errors;

class Project(models.Model):
  title = models.CharField(max_length = 150)
  desc = models.TextField()
  due_date = models.CharField(max_length = 100, null = True)
  admin = models.ForeignKey(User, related_name = 'created_projects', on_delete = models.CASCADE)
  users = models.ManyToManyField(User, related_name = 'assigned_projects')
  is_archived = models.BooleanField(default = False)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)
  objects = ProjectManager()

class Task(models.Model):
  title = models.CharField(max_length = 250)
  desc = models.TextField()
  due_date = models.CharField(max_length = 100, null = True)
  assigned_user = models.ForeignKey(User, related_name = 'assigned_tasks', on_delete = models.CASCADE, null = True)
  project = models.ForeignKey(Project, related_name = 'project_tasks', on_delete = models.CASCADE)
  is_completed = models.BooleanField(default = False)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)
  objects = TaskManager()
 