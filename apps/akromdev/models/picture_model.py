from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.shared.models import AbstractBaseModel


class Picture(AbstractBaseModel):
    image = models.ImageField(upload_to="pictures/images/%Y/%m/%d")
    description = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.image
    
    class Meta:
        verbose_name = _("Picture")
        verbose_name_plural = ("Pictures")
        db_table = "pictures"