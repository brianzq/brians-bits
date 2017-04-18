from django.contrib import admin
from mysite.apps.projects.models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
