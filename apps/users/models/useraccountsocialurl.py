from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.shared.models import AbstractBaseModel


class UserAccountSocialUrl(AbstractBaseModel):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True, null=True)
    url = models.URLField()

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _("Account social url")
        verbose_name_plural = _("Account social urls")
        db_table = "user_account_social_urls"

__all__ = ("UserAccountSocialUrl", )