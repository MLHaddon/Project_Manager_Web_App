from django.urls import path
from . import views

urlpatterns = [
  path('index', views.index),
  path('home', views.home),
  path('create_project', views.create_project),
  path('<int:project_id>/create_task', views.create_task),
  path('<int:project_id>', views.view_tasks),
  path('<int:project_id>/add_member', views.add_member),
  path('<int:user_id>/profile', views.profile),
]