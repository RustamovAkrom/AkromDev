from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.shared.models import AbstractBaseModel
from apps.akromdev.utils import generate_slug


class AudioCategory(AbstractBaseModel):
    name = models.CharField(
        _("name"), max_length=100, help_text=_("Required. 100 charecters")
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _("Audio Category")
        verbose_name_plural = _("Audio Categories")
        db_table = "audio_categories"


class Audio(AbstractBaseModel):
    author = models.ForeignKey(
        "users.UserAccount", models.CASCADE, related_name="audios"
    )
    title = models.CharField(
        _("title"), max_length=120, help_text=_("Required. 120 charecters.")
    )
    slug = models.SlugField(
        _("slug"),
        max_length=200,
        unique=True,
        help_text=_("Required. 200 charecters or fewer."),
        error_messages={"unique": _("With that slug already exists.")},
    )
    description = models.CharField(
        _("description"), max_length=200, blank=True, null=True
    )
    category = models.ForeignKey(
        AudioCategory, models.CASCADE, related_name="audios"
    )
    cover = models.ImageField(_("cover"), upload_to=f"audio/cover/%Y/%m/%d/")
    audio = models.FileField(_("audio"), upload_to=f"audio/audio/%Y/%m/%d/")

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("Audio")
        verbose_name_plural = _("Audios")
        db_table = "audios"
