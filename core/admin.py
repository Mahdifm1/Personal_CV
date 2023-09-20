from django.contrib import admin
from .models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    MAX_OBJECTS = 1

    def has_add_permission(self, request):
        if self.model.objects.count() >= self.MAX_OBJECTS:
            return False
        return super().has_add_permission(request)
