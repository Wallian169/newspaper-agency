from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from manage_app.models import Topic, Newspaper, Redactor


@admin.register(Redactor)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience",)
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("years_of_experience",)}),)
    )
    list_filter = ("years_of_experience", "username")
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "years_of_experience",
                    )
                },
            ),
        )
    )


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("name",)


@admin.register(Newspaper)
class NewspaperAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_display = ("title", "published_date")
    list_filter = ("title", "published_date")
