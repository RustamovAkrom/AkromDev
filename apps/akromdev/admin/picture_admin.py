from django.contrib import admin
from apps.akromdev.models.picture_model import Picture


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    fields = (
        "image",
        "description",
        "author",
    )
    list_display = (
        "image",
        "description",
        "slug",
    )
    search_fields = ("description",)
    list_filter = ("created_at",)
