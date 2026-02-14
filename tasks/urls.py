from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('create/', views.create_project, name='create_project'),
    path('project/<int:project_id>/', views.project_board, name='project_board'),
    path('project/<int:project_id>/add_stage/', views.add_stage, name='add_stage'),
    path('stage/<int:stage_id>/add_task/', views.add_task, name='add_task'),
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
    path('task/<int:task_id>/edit/', views.edit_task, name='edit_task'),
    path('task/<int:task_id>/delete/', views.delete_task, name='delete_task'),
]