DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

CUSTOM_APPS = [
    "apps.akromdev.apps.AkromdevConfig",
    "apps.shared.apps.SharedConfig",
    "apps.users.apps.UsersConfig",
]

THIRD_PARTY_APPS = [
    "phonenumber_field",
    "rest_framework",
    "django_celery_results",
    "django_celery_beat",
    "rest_framework_simplejwt",
    "drf_yasg",
    "django_filters",
    "graphene_django",
]
