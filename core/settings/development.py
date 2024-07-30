from .base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]

INTERNAL_IPS = [
    "127.0.0.1",
]

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.db.DatabaseCache",  # Cache for database
        "LOCATION": "my_cache_table",
    }
}
