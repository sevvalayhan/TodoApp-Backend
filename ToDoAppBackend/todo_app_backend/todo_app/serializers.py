from rest_framework import serializers
from . import models
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        fields = '__all__'