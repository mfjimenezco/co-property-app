"""Production settings."""

from .base import *
from .base import env

# App info
APP_ENV = 'PROD'

# Security
SECRET_KEY = env.str('DJANGO_D_APP_SECRET_KEY')
ALLOWED_HOSTS = env.list('DJANGO_D_APP_ALLOWED_HOSTS')

# Admin
ADMIN_URL = env.str('DJANGO_D_APP_ADMIN_URL')

# Database
DATABASES = {
    'default': {
        'ENGINE': env.str('DJANGO_D_APP_DB_ENGINE'),
        'NAME': env.str('DJANGO_D_APP_DB_NAME'),
        'USER': env.str('DJANGO_D_APP_DB_USER'),
        'PASSWORD': env.str('DJANGO_D_APP_DB_PASSWORD'),
        'HOST': env.str('DJANGO_D_APP_DB_HOST'),
        'PORT': env.int('DJANGO_D_APP_DB_PORT'),
    }
}

# Gunicorn
INSTALLED_APPS += ['gunicorn']
