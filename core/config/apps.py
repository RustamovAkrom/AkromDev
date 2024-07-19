INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    "phonenumber_field",
    
    'apps.akromdev.apps.AkromdevConfig',
    'apps.shared.apps.SharedConfig',
    'apps.users.apps.UsersConfig',
]