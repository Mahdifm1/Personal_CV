from django.contrib import admin
from . import models


@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):
    MAX_OBJECTS = 1

    list_display = ('name', 'short_skills', 'age', 'email')

    def has_add_permission(self, request):
        if self.model.objects.count() >= self.MAX_OBJECTS:
            return False
        return super().has_add_permission(request)


@admin.register(models.Skills)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('skill_name', 'progress_by_percent')


@admin.register(models.Portfolio)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')


@admin.register(models.Work_Experience)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'job_title')


@admin.register(models.Education)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('university_name', 'degree', 'major')


@admin.register(models.Contact_me)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'email', 'is_read_by_admin')
