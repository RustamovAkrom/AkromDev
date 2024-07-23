from django.contrib import admin
from apps.akromdev.models.audio_model import Audio, AudioCategory


@admin.register(Audio)
class AudioAdmin(admin.ModelAdmin):
    fields = (
        "title",
        "description",
        "cover",
        "category",
        "audio",
        "author",
    )
    list_display = (
        "title",
        "slug",
        "description",
        "cover",
        "category",
        "audio",
        "author",
    )
    list_filter = ("created_at",)
    search_fields = (
        "title",
        "slug",
        "description",
    )


@admin.register(AudioCategory)
class AudioCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    list_filter = ("created_at",)
