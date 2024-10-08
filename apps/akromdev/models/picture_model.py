from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.shared.models import AbstractBaseModel
from apps.akromdev.utils import generate_slug


class Picture(AbstractBaseModel):
    author = models.ForeignKey(
        "users.UserAccount", models.CASCADE, related_name="pictures"
    )
    slug = models.SlugField(
        _("slug"),
        unique=True,
        help_text=_("Required. 200 charecters or fewer."),
        error_messages={"unique": _("With that slug already exists.")},
    )
    image = models.ImageField(upload_to="pictures/images/%Y/%m/%d")
    description = models.CharField(
        _("description"), max_length=200, blank=True, null=True
    )

    def __str__(self) -> str:
        return self.image.url

    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.slug)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("Picture")
        verbose_name_plural = "Pictures"
        db_table = "pictures"
