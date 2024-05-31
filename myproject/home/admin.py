from django.contrib import admin
from .models import (Todo, TodoTiming)
# Register your models here.

@admin.register(Todo)
class AdminTodo(admin.ModelAdmin):
    list_display = ['todo_title', 'todo_description', 'is_done', 'todo_age']
    list_per_page = 10
    search_fields = ['todo_title']

@admin.register(TodoTiming)
class TimingTodo(admin.ModelAdmin):
    list_display = ['todo', 'timing']
    list_per_page = 10
    search_fields = ['todo']