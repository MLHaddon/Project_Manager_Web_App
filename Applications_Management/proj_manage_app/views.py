from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from login_app.models import User
from .models import Project, Task, Favorite

#! Redirects

def index(request):
  if not 'user_id' in request.session:
    messages.error(request, 'You must be logged in to do that.')
    return redirect('/main')
  return redirect('/proj_manage/home')

def create_project(request):
  if not 'user_id' in request.session:
    messages.error(request, 'You must be logged in to do that.')
    return redirect('/main')

  errors = Project.objects.basic_validator(request.POST)
  if errors:
    for key, val in errors.items():
      messages.error(request, val)
      return redirect('/proj_manage/home')

  Project.objects.create(
    title = request.POST['title'],
    desc = request.POST['desc'],
    due_date = request.POST['due'],
    admin = User.objects.get(id = request.session['user_id']),
  )
  project = Project.objects.get(title = request.POST['title'], desc = request.POST['desc'])
  project.users.add(project.admin)
  project.save()
  return redirect('/proj_manage/home')

def create_task(request, project_id):
  if not 'user_id' in request.session:
    messages.error(request, 'You must be logged in to do that.')
    return redirect('/main')

  errors = Project.objects.basic_validator(request.POST)
  if errors:
    for key, val in errors.items():
      messages.error(request, val)
      return redirect(f'/proj_manage/{project_id}')
  
  Task.objects.create(
    title = request.POST['title'],
    desc = request.POST['desc'],
    due_date = request.POST['due'],
    assigned_user = User.objects.get(id = request.POST['user']),
    project = Project.objects.get(id = project_id)
  )
  return redirect(f'/proj_manage/{project_id}')

def add_member(request, project_id):
  if not 'user_id' in request.session:
    messages.error(request, 'You must be logged in to do that.')
    return redirect('/main')
  project = Project.objects.get(id = project_id)
  newMember = User.objects.get(id = request.POST['member'])
  project.users.add(newMember)
  print(project.users.all())
  project.save()
  return redirect('/proj_manage/home')

def archive(request, project_id):
  if not 'user_id' in request.session:
    messages.error(request, 'You must be logged in to do that.')
    return redirect('/main')
  project = Project.objects.get(id = project_id)
  project.is_archived = True
  project.save()
  return redirect('/proj_manage/home')

def un_archive(request, project_id):
  if not 'user_id' in request.session:
    messages.error(request, 'You must be logged in to do that.')
    return redirect('/main')
  project = Project.objects.get(id = project_id)
  project.is_archived = False
  project.save()
  return redirect('/proj_manage/home')

def completed(request, project_id, task_id):
  if not 'user_id' in request.session:
    messages.error(request, 'You must be logged in to do that.')
    return redirect('/main')
  task = Task.objects.get(id = task_id)
  task.is_completed = True
  task.save()
  return redirect(f'/proj_manage/{project_id}')

def un_complete(request, project_id, task_id):
  if not 'user_id' in request.session:
    messages.error(request, 'You must be logged in to do that.')
    return redirect('/main')
  task = Task.objects.get(id = task_id)
  task.is_completed = False
  task.save()
  return redirect(f'/proj_manage/{project_id}')

def favorite(request):
  theyLikedIt = Favorite.objects.get(id = 1)
  theyLikedIt.count += 1
  theyLikedIt.save()
  return redirect('/proj_manage/home')

#! Direct Links

def home(request):
  if not 'user_id' in request.session:
    messages.error(request, 'You must be logged in to do that.')
    return redirect('/main')
  context = {
    'user': User.objects.get(id = request.session['user_id']),
    'users': User.objects.all(),
    'projects': Project.objects.all(),
    'fav': Favorite.objects.get(id = 1)
  }
  return render(request, 'home.html', context)

def view_tasks(request, project_id):
  if not 'user_id' in request.session:
    messages.error(request, 'You must be logged in to do that.')
    return redirect('/main')
  context = {
    'user': User.objects.get(id = request.session['user_id']),
    'users': User.objects.all(),
    'project': Project.objects.get(id = project_id),
  }
  return render(request, 'tasks.html', context)

def profile(request, user_id):
  if not 'user_id' in request.session:
    messages.error(request, 'You must be logged in to do that.')
    return redirect('/main')
  context = {
    'user': User.objects.get(id = request.session['user_id']),
    'profile_user': User.objects.get(id = user_id),
    'users': User.objects.all(),
    'user_projects': Project.objects.filter(admin = User.objects.get(id = user_id)),
    'user_tasks':  Task.objects.filter(assigned_user = User.objects.get(id = user_id)) 
  }
  return render(request, 'profile.html', context)
