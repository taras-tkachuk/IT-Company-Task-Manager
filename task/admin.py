from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from task.models import Worker, TaskType, Position, Tag, Task


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position",)
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("position",)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "position",
                    )
                },
            ),
        )
    )


admin.site.register(TaskType)
admin.site.register(Position)
admin.site.register(Tag)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ("name", )
    list_filter = ("assignees", "task_type", "tags", "priority")
