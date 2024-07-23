from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.shared.models import AbstractBaseModel


class AboutSocialUrl(AbstractBaseModel):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True, null=True)
    url = models.URLField()

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _("About social url")
        verbose_name_plural = _("Avout social urls")
        db_table = "about_social_urls"


class About(AbstractBaseModel):
    user = models.OneToOneField("users.User", models.CASCADE, related_name="user_about")
    title = models.CharField(max_length=120)
    content = models.TextField()
    social = models.ManyToManyField(
        AboutSocialUrl, related_name="url_about", blank=True
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = _("About")
        verbose_name_plural = _("Abouts")
        db_table = "abouts"
