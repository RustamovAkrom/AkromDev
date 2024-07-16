from django.contrib import admin
from apps.akromdev.models.picture_model import Picture


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ("image", "description", )
    search_fields = ("description", )
    list_filter = ("created_at", )