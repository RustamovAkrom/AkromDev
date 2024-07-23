from django.contrib import admin
from apps.akromdev.models.contact_model import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
    )
    search_fields = (
        "name",
        "email",
        "subject",
    )
    list_filter = ("created_at",)
