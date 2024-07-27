from django.contrib import admin
from apps.users.models.useraccountsocialurl import UserAccountSocialUrl


@admin.register(UserAccountSocialUrl)
class UseraccountSocialUrlAdmin(admin.ModelAdmin):
    pass


__all__ = ("UseraccountSocialUrlAdmin", )