
"""Production settings."""

from .base import *
from .base import env

# App info
APP_ENV = ''

# Base
SECRET_KEY = env('DJANGO_D_APP_SECRET_KEY')
ALLOWED_HOSTS = env.list('DJANGO_D_APP_ALLOWED_HOSTS')

# Admin
ADMIN_URL = env('DJANGO_D_APP_ADMIN_URL')

# Gunicorn
INSTALLED_APPS += ['gunicorn']

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