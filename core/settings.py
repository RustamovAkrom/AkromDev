from django.utils.translation import gettext_lazy as _

from pathlib import Path
import os

from .config import *
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv("envs/.env"))


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY", "1")

DEBUG = os.getenv("DEBUG", 1)

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = CUSTOM_APPS + DJANGO_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",  # Translation middleware
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

import dj_database_url


DATABASES = {
    "default": dj_database_url.parse(os.getenv("DATABASE_URL"))
}
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR.joinpath("db.sqlite3"),
#     }
# }

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": os.getenv("NAME"),
#         "USER": os.getenv("USER"),
#         "PASSWORD": os.getenv("PASSWORD"),
#         "HOST": os.getenv("HOST"),
#         "PORT": os.getenv("PORT"),
#         "TEST": {"NAME": "test_akromdev_db_2"}
#     }
# }

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGES = (
    ("en", _("English")),
    ("ru", _("Russian")),
    ("uz", _("Uzbek")),
)
LANGUAGE_CODE = "en-us"

LOCALE_PATHS = (BASE_DIR.joinpath("locale"),)

USE_I18N = True

TIME_ZONE = "Asia/Tashkent"

USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

STATIC_URL = "static/"
MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR.joinpath("media")
STATIC_ROOT = BASE_DIR.joinpath("staticfiles")

STATICFILES_DIRS = [BASE_DIR.joinpath("static")]

# Debut Toolbar
INTERNAL_IPS = [
    "127.0.0.1",
]

# CACHES = {
#     'default': {
#         "BACKEND": "django.core.cache.backends.redis.RedisCache", # Cache for redis
#         "LOCATION": "redis://localhost:6279/1"
#     },
# }

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.db.DatabaseCache", # Cache for database
        "LOCATION": "my_cache_table",
    }
}

# Email
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = True