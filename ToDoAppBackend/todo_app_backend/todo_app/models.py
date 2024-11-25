from typing import Any
from django.db import models
from django.utils import timezone
from django.db import models

class Priority(models.TextChoices):
    URGENT = 'urgent', 'Urgent'
    HIGH = 'high', 'High'
    MEDIUM = 'medium', 'Medium'
    LOW = 'low', 'Low'

class Task(models.Model):
    def __str__(self) -> str:
        return f"{self.title}  {self.date}"
    title= models.CharField(max_length=20,null=False)
    description = models.TextField(max_length=100,null=False)
    is_complated= models.BooleanField(default=False)
    created_at= models.DateTimeField(default=timezone.now)
    date = models.TextField()
    priority = models.TextField(choices=Priority.choices)
    class Meta:
        db_table= "tasks"