from django.contrib import admin
from .models import Profile, Project, Skill, Education, Contact

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'email', 'created_at', 'updated_at')
    search_fields = ('name', 'title', 'bio')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'is_ongoing', 'created_at')
    list_filter = ('is_ongoing', 'created_at')
    search_fields = ('title', 'description')
    filter_horizontal = ('technologies',)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'level', 'created_at')
    list_filter = ('category', 'level')
    search_fields = ('name',)

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('school_name', 'degree', 'field_of_study', 'start_date', 'end_date', 'is_current')
    list_filter = ('is_current', 'degree')
    search_fields = ('school_name', 'degree', 'field_of_study')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
