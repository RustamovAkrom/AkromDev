from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.shared.models import AbstractBaseModel


class AboutSocialUrl(AbstractBaseModel):
    name = models.CharField(
        _("name"), max_length=100, help_text=_("Required. 100 charecters.")
    )
    description = models.CharField(
        _("description"),
        max_length=200,
        blank=True,
        null=True,
        help_text=_("200 charecters."),
    )
    url = models.URLField(_("url"))

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _("About social url")
        verbose_name_plural = _("Avout social urls")
        db_table = "about_social_urls"


class About(AbstractBaseModel):
    user = models.OneToOneField("users.User", models.CASCADE, related_name="user_about")
    title = models.CharField(
        _("title"), max_length=120, help_text=_("Required. 120 charecters.")
    )
    content = models.TextField(_("content"), help_text=(_("Required.")))
    social = models.ManyToManyField(
        AboutSocialUrl, related_name="url_about", blank=True
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = _("About")
        verbose_name_plural = _("Abouts")
        db_table = "abouts"
