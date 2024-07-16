from django.contrib import admin
from apps.akromdev.models.blog_model import Post, PostComment, PostCommentLike, PostLike, PostContent


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "is_active", "author", )
    search_fields = ("title", "slug", )
    list_filter = ("created_at", )


@admin.register(PostContent)
class PostContentAdmin(admin.ModelAdmin):
    list_display = ("content", "image", "file", )
    search_fields = ("content", )
    list_filter = ("created_at", )


@admin.register(PostComment)
class PostCommenAdmin(admin.ModelAdmin):
    list_display = ("message", )
    search_fields = ("message", )
    list_filter = ("created_at", )


@admin.register(PostCommentLike)
class PostCommentLikeAdmin(admin.ModelAdmin):
    list_display = ("comment", "user", )
    search_fields = ("comment", "user", )
    list_filter = ("created_at", )


@admin.register(PostLike)
class PostLikeAdmin(admin.ModelAdmin):
    list_display = ("post", "user", )
    search_fields = ("post", "user", )
    list_filter = ("created_at", )