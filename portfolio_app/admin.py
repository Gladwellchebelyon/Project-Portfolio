from django.contrib import admin
from .models import Project, Contact, Skill  # Import only necessary models

# Register models properly
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'insights', 'demo_url', 'github_url')
    search_fields = ('title', 'description')  # Allow searching by title and description
    list_filter = ('demo_url', 'github_url')  # Filter by demo_url or github_url

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
    search_fields = ('name', 'email')  # Allow searching by name and email

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)  # Allow searching by skill name



