from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from django.views.generic import View
from django.http import JsonResponse
from .forms import TaskForm

class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class AddTaskView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class UpdateTaskView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class=TaskSerializer
    lookup_field='pk'


class DeleteTaskView(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'pk'