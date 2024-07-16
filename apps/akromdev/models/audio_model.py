from django.db import models 
from django.utils.translation import gettext_lazy as _
from apps.shared.models import AbstractBaseModel
from apps.akromdev.utils import generate_slug


class Audio(AbstractBaseModel):
    author = models.ForeignKey("users.User", models.CASCADE, related_name="audios")
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    cover = models.ImageField(upload_to=f"audio/cover/%Y/%m/%d/")
    audio = models.FileField(upload_to=f"audio/audio/%Y/%m/%d/")

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        return super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = _("Audio")
        verbose_name_plural = _("Audios")
        db_table = "audios"


class AudioCategory(AbstractBaseModel):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = _("Audio Category")
        verbose_name_plural = _("Audio Categories")
        db_table = "audio_categories"
