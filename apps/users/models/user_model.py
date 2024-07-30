from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from apps.users.utils import generate_token


class User(AbstractUser):
    token = models.CharField(
        max_length=200,
        unique=True,
        help_text=_("Required. 200 charecters unique !"),
        error_messages={"unique": _("A user with that token already exists")},
        db_index=True,
    )
    folowings = models.ManyToManyField(
        "self", symmetrical=False, related_name="folowers", blank=True, db_index=True
    )

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        db_table = "users"

    def save(self, *args, **kwargs):
        self.token = generate_token(200)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.username


__all__ = ("User",)
