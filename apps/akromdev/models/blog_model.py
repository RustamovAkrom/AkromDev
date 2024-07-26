from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.shared.models import AbstractBaseModel
from apps.akromdev.utils import generate_slug


class Post(AbstractBaseModel):
    author = models.ForeignKey(
        "users.UserAccount", models.CASCADE, related_name="posts"
    )
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200, unique=True)
    bg_image = models.ImageField(upload_to="blog/images/%Y/%m/%d", blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField()
    is_active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
        db_table = "posts"


class PostComment(AbstractBaseModel):
    post = models.ForeignKey(Post, models.CASCADE, related_name="comments")
    user = models.ForeignKey("users.User", models.CASCADE, related_name="comments")
    message = models.TextField()

    def __str__(self) -> str:
        return self.message

    class Meta:
        verbose_name = _("Post comment")
        verbose_name_plural = _("Post Comments")
        db_table = "post_comments"


class PostLike(AbstractBaseModel):
    post = models.ForeignKey(Post, models.DO_NOTHING, related_name="post_likes")
    user = models.ForeignKey("users.User", models.CASCADE, related_name="post_likes")

    def __str__(self) -> str:
        return f"({self.user}) to like post ({self.post})"

    def like_count(self):
        return self.user.objects.count()

    class Meta:
        verbose_name = _("Post like")
        verbose_name_plural = _("Post likes")
        db_table = "post_likes"


class PostCommentLike(AbstractBaseModel):
    comment = models.ForeignKey(
        PostComment, models.CASCADE, related_name="post_comment_likes"
    )
    user = models.ForeignKey(
        "users.User", models.DO_NOTHING, related_name="post_comment_likes"
    )

    def __str__(self) -> str:
        return f"({self.user} to like comment ({self.comment}))"

    class Meta:
        verbose_name = _("Post comment like")
        verbose_name_plural = _("Post comment likes")
        db_table = "post_comment_likes"
