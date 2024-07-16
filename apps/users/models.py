from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from apps.shared.models import AbstractBaseModel
from .utils import generate_token


class User(AbstractUser):
    token = models.CharField(
        max_length=200, 
        unique=True, 
        help_text=_("Required. 200 charecters unique !"), 
        error_messages={"unique":_("A user with that token already exists")},
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
        ("f", "Female"),
        ("m", "Male"),
    ]

    user = models.ForeignKey("users.User", models.CASCADE, related_name="account", db_index=True)
    avatar = models.ImageField(upload_to="avatar/images/avatar/%Y/%m/%d", blank=True, null=True, default="avatar/default/avatar.jpg")
    bio = models.CharField(max_length=300, blank=True, null=True)
    bg_account_image = models.ImageField(upload_to="account/images/bg/%Y/%m/%d", blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    phone_number = PhoneNumberField(blank=True, null=True, region="UZ")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    socials = models.ManyToManyField(UserAccountSocialUrl, related_name="user_acccount", db_index=True)
    is_premium = models.BooleanField(default=False)

    def follow(self, user):
        self.user.folowings.add(user)

    def unfollow(self, user):
        self.user.folowings.remove(user)
    
    class Meta:
        verbose_name = _("User account")
        verbose_name_plural = _("User accounts")
        db_table = "user_accounts"

    def __str__(self) -> str:
        return f"@{self.user.username}"
    