from .base import *


DEBUG = False

ALLOWED_HOSTS = []

# import dj_database_url

# DATABASES = {
#     "default": dj_database_url.parse(os.getenv("DATABASE_URL"))
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("NAME"),
        "USER": os.getenv("USER"),
        "PASSWORD": os.getenv("PASSWORD"),
        "HOST": os.getenv("HOST"),
        "PORT": os.getenv("PORT"),
        "TEST": {"NAME": "test_akromdev_db_2"},
    }
}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",  # Cache for redis
        "LOCATION": "redis://localhost:6279/1",
    },
}
