"""Development settings."""

from .base import *
from .base import env

# App info
APP_ENV = 'DEV'

# Base
DEBUG = True

# Security
SECRET_KEY = env('DJANGO_D_APP_SECRET_KEY', default='django-insecure-development-key')
ALLOWED_HOSTS = ["*"]