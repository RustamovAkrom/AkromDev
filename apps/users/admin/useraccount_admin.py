from django.contrib import admin
from apps.users.models.useraccount_model import UserAccount


@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
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


__all__ = ("UserAccountAdmin",)
