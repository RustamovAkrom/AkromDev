from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.shared.models import AbstractBaseModel


class Contact(AbstractBaseModel):
    name = models.CharField(
        _("name"), max_length=100, help_text=_("Required. 100 charecters.")
    )
    email = models.EmailField(
        _("email address"), max_length=120, help_text=_("Required. 120 charecters.")
    )
    subject = models.CharField(
        _("subject"), max_length=100, help_text=_("Required. 100 charecters")
    )
    message = models.TextField(_("message"), help_text=_("Required."))

    def __str__(self) -> str:
        return self.message

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")
        db_table = "contacts"
