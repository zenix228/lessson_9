from django.contrib import admin
from .models import CustomUser, Project, Task

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username')
    list_display_links = ('id', 'username')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'start_date', 'end_date')
    list_display_links = ('id', 'title', 'start_date', 'end_date')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'deadline_date', 'completed')
    list_display_links = ('id', 'title', 'deadline_date', 'completed')