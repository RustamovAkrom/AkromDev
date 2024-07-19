from django.contrib import admin
from apps.akromdev.models.video_model import Video, VideoCategory, VideoLike, VideoComment


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    fields = ("author", "title", "description", "content", "cover", "video", "category", "watched", )
    list_display = ("title", "slug", "description", )
    search_fields = ("title", "slug", )
    list_filter = ("created_at", )
    
@admin.register(VideoCategory)
class VideoCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", )
    search_fields = ("name", )
    list_filter = ("created_at", )


@admin.register(VideoLike)
class VideoLikeAdmin(admin.ModelAdmin):
    list_display = ("video", "user", )
    search_fields = ("video", "user", )
    list_filter = ("created_at", )


@admin.register(VideoComment)
class VideoCommentAdmin(admin.ModelAdmin):
    list_display = ("message", )
    search_fields = ("message", )
    list_filter = ("created_at", )