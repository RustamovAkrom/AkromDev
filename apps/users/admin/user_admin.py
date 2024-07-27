from django.contrib import admin
from apps.users.models.user_model import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass



__all__ = ("UserAdmin", )