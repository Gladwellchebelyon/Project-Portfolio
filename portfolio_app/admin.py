from django.contrib import admin
from django.utils.html import format_html
from .models import Project, Skill, Contact, TechIcon

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'demo_url', 'github_url')
    search_fields = ('title', 'description')
    list_filter = ('demo_url', 'github_url')

@admin.register(TechIcon)
class TechIconAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon_preview', 'class_name', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'class_name')
    ordering = ('category', 'name')
    
    def icon_preview(self, obj):
        return format_html('<i class="{}" style="font-size: 1.5em;"></i>', obj.class_name)
    icon_preview.short_description = 'Icon'

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon_display', 'proficiency')
    list_editable = ('proficiency',)
    search_fields = ('name', 'icon__name')
    list_filter = ('proficiency', 'icon__category')
    ordering = ('-proficiency',)
    
    def icon_display(self, obj):
        if obj.icon:
            return format_html(
                '<i class="{}" style="font-size: 1.5em;"></i> {} ({})',
                obj.icon.class_name,
                obj.icon.name,
                obj.icon.get_category_display()
            )
        return "No icon selected"
    icon_display.short_description = 'Icon'

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')



