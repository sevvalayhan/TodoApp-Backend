from django.urls import path
from . import views

urlpatterns = [
    path('gettodo',views.TaskListView.as_view()),
    path('add-task',views.AddTaskView.as_view()),
    path('update-task/<int:pk>',views.UpdateTaskView.as_view()),
    path('delete-task/<int:pk>',views.DeleteTaskView.as_view())
]