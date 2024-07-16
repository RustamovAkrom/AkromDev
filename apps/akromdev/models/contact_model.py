from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.shared.models import AbstractBaseModel


class Contact(AbstractBaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=120)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self) -> str:
        return self.message
    
    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")
        db_table = "contacts"

        