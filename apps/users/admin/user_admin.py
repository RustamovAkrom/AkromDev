from django.contrib import admin
from apps.users.models.user_model import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "first_name",
        "last_name",
    )
    search_fields = (
        "username",
        "first_name",
        "last_name",
    )


__all__ = ("UserAdmin",)
