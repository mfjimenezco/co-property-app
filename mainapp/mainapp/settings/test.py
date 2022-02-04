"""Testing settings.
With these settings, tests run faster.
"""

from .base import *
from .base import env

# App info
APP_ENV = 'TEST'

# Base
DEBUG = True

# Security
SECRET_KEY = env('DJANGO_D_APP_SECRET_KEY', default='django-insecure-test-key')
ALLOWED_HOSTS = env.list('DJANGO_D_APP_ALLOWED_HOSTS')

TEST_RUNNER = "django.test.runner.DiscoverRunner"

# Passwords
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('DJANGO_D_APP_DB_NAME'),
        'USER': env('DJANGO_D_APP_DB_USER'),
        'PASSWORD': env('DJANGO_D_APP_DB_PASSWORD'),
        'HOST': env('DJANGO_D_APP_DB_HOST'),
        'PORT': env('DJANGO_D_APP_DB_PORT'),
    }
}