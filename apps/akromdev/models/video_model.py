from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.shared.models import AbstractBaseModel
from apps.akromdev.utils import generate_slug


class Video(AbstractBaseModel):
    author = models.ForeignKey("users.UserAccount", models.CASCADE, related_name="videos")
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=200, unique=True, db_index=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField()
    cover = models.ImageField(upload_to=f"video/{slug}/covers/%Y/%m/%d/")
    video = models.FileField(upload_to=f"video/{slug}/videos/%Y/%m/%d/")
    category = models.ForeignKey("akromdev.VideoCategory", models.CASCADE, related_name="videos")
    watched = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = _("Video")
        verbose_name_plural = ("Videos")


class VideoCategory(AbstractBaseModel):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = _("Video category")
        verbose_name_plural = _("Video categories")


class VideoComment(AbstractBaseModel):
    video = models.ForeignKey(Video, models.CASCADE, related_name="comments")
    user = models.ForeignKey("users.User", models.CASCADE, related_name="video_comments")
    message = models.TextField()

    def __str__(self) -> str:
        return self.message
    
    class Meta:
        verbose_name = _("Video comment")
        verbose_name_plural = _("Video comments")
        db_table = "video_comments"


class VideoLike(AbstractBaseModel):
    video = models.ForeignKey(Video, models.CASCADE, related_name="video_likes")
    user = models.ForeignKey("users.User", models.DO_NOTHING, related_name="video_likes")

    def __str__(self) -> str:
        return f"({self.user}) to like video ({self.video})"
    
    class Meta:
        verbose_name = _("Video like")
        verbose_name_plural = _("Video likes")
        db_table = "video_likes"