from django.contrib import admin
from apps.users.models.useraccount_model import UserAccount


@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    pass


__all__ = ("UserAccountAdmin", )