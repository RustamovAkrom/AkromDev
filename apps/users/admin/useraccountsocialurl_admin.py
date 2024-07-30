from django.contrib import admin
from apps.users.models.useraccountsocialurl import UserAccountSocialUrl


@admin.register(UserAccountSocialUrl)
class UseraccountSocialUrlAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "url",
    )
    search_fields = (
        "name",
        "description",
    )


__all__ = ("UseraccountSocialUrlAdmin",)
