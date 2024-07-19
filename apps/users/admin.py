from django.contrib import admin
from .models import User, UserAccount, UserAccountSocialUrl


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    pass


@admin.register(UserAccountSocialUrl)
class UseraccountSocialUrlAdmin(admin.ModelAdmin):
    pass

