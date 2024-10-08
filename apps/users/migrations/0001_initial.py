# Generated by Django 5.0.3 on 2024-07-29 06:20

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserAccountSocialUrl",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now=True)),
                ("name", models.CharField(max_length=100)),
                (
                    "description",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("url", models.URLField()),
            ],
            options={
                "verbose_name": "Account social url",
                "verbose_name_plural": "Account social urls",
                "db_table": "user_account_social_urls",
            },
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "token",
                    models.CharField(
                        db_index=True,
                        error_messages={
                            "unique": "A user with that token already exists"
                        },
                        help_text="Required. 200 charecters unique !",
                        max_length=200,
                        unique=True,
                    ),
                ),
                (
                    "folowings",
                    models.ManyToManyField(
                        blank=True,
                        db_index=True,
                        related_name="folowers",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "db_table": "users",
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="UserAccount",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now=True)),
                (
                    "first_name",
                    models.CharField(
                        blank=True,
                        help_text="100 charecters.",
                        max_length=100,
                        null=True,
                        verbose_name="first name",
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True,
                        help_text="100 charecters.",
                        max_length=100,
                        null=True,
                        verbose_name="last name",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        blank=True,
                        help_text="Required. 150 charecters or fewer. Latters, digits and @/./+/-/_ only.",
                        max_length=150,
                        verbose_name="username",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=150, verbose_name="email address"
                    ),
                ),
                (
                    "avatar",
                    models.ImageField(
                        blank=True,
                        default="avatar/default/avatar.jpg",
                        null=True,
                        upload_to="avatar/images/avatar/%Y/%m/%d",
                        verbose_name="user avatar image",
                    ),
                ),
                (
                    "bg_cover",
                    models.ImageField(
                        blank=True,
                        default="bg/default/bg.jpg",
                        null=True,
                        upload_to="bg/images/%Y/%m/%d",
                        verbose_name="account baground cover",
                    ),
                ),
                (
                    "bio",
                    models.CharField(
                        blank=True, max_length=300, null=True, verbose_name="bio"
                    ),
                ),
                (
                    "birthday",
                    models.DateField(blank=True, null=True, verbose_name="birth day"),
                ),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True,
                        max_length=128,
                        null=True,
                        region="UZ",
                        verbose_name="phone number",
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        blank=True,
                        choices=[("f", "Female"), ("m", "Male")],
                        max_length=1,
                        null=True,
                        verbose_name="gender",
                    ),
                ),
                (
                    "country",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="country"
                    ),
                ),
                (
                    "is_premium",
                    models.BooleanField(default=False, verbose_name="premium"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="account",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "socials",
                    models.ManyToManyField(
                        blank=True,
                        db_index=True,
                        related_name="user_acccount",
                        to="users.useraccountsocialurl",
                    ),
                ),
            ],
            options={
                "verbose_name": "User account",
                "verbose_name_plural": "User accounts",
                "db_table": "user_accounts",
            },
        ),
    ]
