from django.contrib import admin
from .models import (
    CustomUser,
    Task
)


class CustomUserAdmin(admin.ModelAdmin):
    pass


class TaskAdmin(admin.ModelAdmin):
    pass


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Task, TaskAdmin)