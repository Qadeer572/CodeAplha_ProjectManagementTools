from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'projects'

urlpatterns = [
    path('', views.projects, name='projects'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/<int:task_id>/comment/', views.add_comment, name='add_comment'),
    path('tasks/<int:task_id>/message/', views.send_message, name='send_message'),
    path('new-project/', views.newProject, name='new-project'),
    path('new-task/', views.newTask, name='new-task'),
]