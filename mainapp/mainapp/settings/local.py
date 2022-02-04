"""Development settings."""

from .base import *
from .base import env

# App info
APP_ENV = 'DEV'

# Security
SECRET_KEY = 'django-insecure-development-key'
ALLOWED_HOSTS = ["*"]
DEBUG = True

# Admin
ADMIN_URL = 'admin/'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}