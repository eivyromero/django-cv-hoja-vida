from django.contrib import admin
from .models import (
    Profile, Skill, Experience, Education,
    Course, Award, Project, Service, Task
)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'email', 'phone']
    
    def has_add_permission(self, request):
        # Solo permitir un perfil
        return not Profile.objects.exists()


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'level', 'order']
    list_filter = ['category']
    search_fields = ['name']
    ordering = ['category', 'order', 'name']


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['position', 'company', 'start_date', 'end_date', 'is_current', 'order']
    list_filter = ['is_current']
    search_fields = ['company', 'position']
    ordering = ['-order', '-start_date']


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution', 'start_date', 'end_date', 'is_current', 'order']
    list_filter = ['is_current']
    search_fields = ['institution', 'degree']
    ordering = ['-order', '-start_date']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'institution', 'date', 'duration', 'order']
    search_fields = ['name', 'institution']
    ordering = ['-order', '-date']


@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ['title', 'organization', 'date', 'order']
    search_fields = ['title', 'organization']
    ordering = ['-order', '-date']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'start_date', 'is_featured', 'order']
    list_filter = ['is_featured']
    search_fields = ['title', 'description']
    ordering = ['-order', '-start_date']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'order']
    list_filter = ['is_active']
    search_fields = ['name', 'description']
    ordering = ['order', 'name']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'important', 'created', 'datecompleted']
    list_filter = ['important', 'user']
    search_fields = ['title', 'description']
    ordering = ['-created']