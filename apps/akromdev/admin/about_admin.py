from django.contrib import admin
from apps.akromdev.models.about_model import About, AboutSocialUrl


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "user", )
    list_filter = ('created_at', )
    search_fields = ("title", "content", )


@admin.register(AboutSocialUrl)
class AboutSocialUrlAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "url", )
    list_filter = ("created_at", )
    search_fields = ("name", "description", "url", )