from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from apps.shared.models import AbstractBaseModel
from .utils import generate_token

from core.config import auth
import os


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


class UserAccount(AbstractBaseModel):
    GENDER_CHOICES = [
        ("f", _("Female")),
        ("m", _("Male")),
    ]

    user = models.ForeignKey(
        "users.User", models.DO_NOTHING, related_name="account", db_index=True
    )
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=150, blank=True)
    email = models.EmailField(max_length=150, blank=True)
    avatar = models.ImageField(
        upload_to="avatar/images/avatar/%Y/%m/%d",
        blank=True,
        null=True,
        default=auth.USER_ACCOUNT_DEFAULT_IMG + auth.USER_ACCOUNT_IMG_NAME,
    )
    bg_cover = models.ImageField(
        upload_to="bg/images/%Y/%m/%d",
        blank=True,
        null=True,
        default=auth.USER_ACCOUNT_BG_DEFAULT_IMG + auth.USER_ACCOUNT_BG_IMG_NAME,
    )
    bio = models.CharField(max_length=300, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    phone_number = PhoneNumberField(blank=True, null=True, region="UZ")
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, blank=True, null=True
    )
    country = models.CharField(max_length=50, blank=True, null=True)
    socials = models.ManyToManyField(
        UserAccountSocialUrl, related_name="user_acccount", db_index=True, blank=True
    )
    is_premium = models.BooleanField(default=False)

    def follow(self, user):
        self.user.folowings.add(user)

    def unfollow(self, user):
        self.user.folowings.remove(user)

    def save(self, *args, **kwargs):

        if self.username[0] != "@":
            self.username = "@" + self.username

        self.user.first_name = self.first_name
        self.user.last_name = self.last_name
        self.user.email = self.email
        if self.username[0] == "@":
            self.user.username = self.username[1:]
        else:
            self.user.username = self.username
        self.user.save()

        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("User account")
        verbose_name_plural = _("User accounts")
        db_table = "user_accounts"

    def __str__(self) -> str:
        return self.username
