from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.

class Base(models.Model):
    uuid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    class Meta:
        abstract = True

class Todo(Base):
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    todo_title = models.CharField(max_length=100, null=True, blank=True)
    todo_description = models.TextField()
    todo_age = models.PositiveIntegerField(default=18, null=True, blank=True)
    is_done = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.todo_title or self.todo_description
    
class TodoTiming(Base):
    
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    timing = models.DateField()
    
    def __str__(self):
        return self.todo.todo_title
    