from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.shared.models import AbstractBaseModel
from apps.akromdev.utils import generate_slug


class Video(AbstractBaseModel):
    author = models.ForeignKey(
        "users.UserAccount", models.CASCADE, related_name="videos"
    )
    title = models.CharField(
        _("title"),
        max_length=150,
        db_index=True,
        help_text=_("Required. 150 charecters"),
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        db_index=True,
        help_text=_("Required. 200 charecters or fewer."),
        error_messages={"unique": _("With that slug already exists.")},
    )
    description = models.CharField(
        _("description"), max_length=200, blank=True, null=True
    )
    content = models.TextField(_("content"), help_text=_("Required."))
    cover = models.ImageField(upload_to=f"video/covers/%Y/%m/%d/")
    video = models.FileField(upload_to=f"video/videos/%Y/%m/%d/")
    category = models.ForeignKey(
        "akromdev.VideoCategory", models.CASCADE, related_name="videos"
    )
    watched = models.IntegerField(_("watched"), default=0)

    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = _("Video")
        verbose_name_plural = "Videos"


class VideoCategory(AbstractBaseModel):
    name = models.CharField(
        _("name"), max_length=100, help_text=_("Required. 100 charecters")
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _("Video category")
        verbose_name_plural = _("Video categories")


class VideoComment(AbstractBaseModel):
    video = models.ForeignKey(Video, models.CASCADE, related_name="comments")
    user = models.ForeignKey(
        "users.UserAccount", models.CASCADE, related_name="video_comments"
    )
    message = models.TextField(_("message"), help_text=_("Required."))

    def __str__(self) -> str:
        return self.message

    class Meta:
        verbose_name = _("Video comment")
        verbose_name_plural = _("Video comments")
        db_table = "video_comments"


class VideoLike(AbstractBaseModel):
    video = models.ForeignKey(Video, models.CASCADE, related_name="video_likes")
    user = models.ForeignKey(
        "users.UserAccount", models.DO_NOTHING, related_name="video_likes"
    )

    def __str__(self) -> str:
        return f"({self.user}) to like video ({self.video})"

    class Meta:
        verbose_name = _("Video like")
        verbose_name_plural = _("Video likes")
        db_table = "video_likes"
