from django.urls import path
from . import views

urlpatterns = [
  path('index', views.index),
  path('home', views.home),
  path('favorite', views.favorite),
  path('create_project', views.create_project),
  path('<int:project_id>/create_task', views.create_task),
  path('<int:project_id>', views.view_tasks),
  path('<int:user_id>/profile', views.profile),
  path('<int:project_id>/add_member', views.add_member),
  path('<int:project_id>/archive', views.archive),
  path('<int:project_id>/un_archive', views.un_archive),
  path('<int:project_id>/<int:task_id>/completed', views.completed),
  path('<int:project_id>/<int:task_id>/un_complete', views.un_complete),
  path('<int:project_id>/<int:task_id>/assign_task', views.assign_task),
]