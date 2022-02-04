"""
Django settings for mainapp project.
"""

# -*- coding: utf-8 -*-

import environ
from pathlib import Path

# App info
APP_NAME = 'Application'
APP_SUB_NAME = 'APP'
APP_SHORT_NAME = 'APP'
APP_LONG_NAME = 'Django AdminLTE Application Base'
APP_COMPANY = 'mfjimenezco'
APP_VERSION = 'v0.0.0'

BASE_DIR = Path(__file__).resolve().parent.parent.parent

env = environ.Env()

# Security
DEBUG = env.bool('DJANGO_D_APP_DEBUG', default=False)

# Internationalization
LANGUAGE_CODE = 'en'
TIME_ZONE = env.str('DJANGO_D_APP_TIME_ZONE', default='UTC')
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = (
    ('en', 'English'),
    ('es', 'Español'),
)

LOCALE_PATHS = (
    BASE_DIR / 'locale',
)

WSGI_APPLICATION = 'mainapp.wsgi.application'

# Application definition
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
]

LOCAL_APPS = [
    'mainapp',
    'accounts',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# Passwords
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
]

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Middlewares
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    
    'accounts.middlewares.ProfileCompleteMiddleware',
]

# URLs
ROOT_URLCONF = 'mainapp.urls'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

# Media files
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Login
LOGIN_URL = '/accounts/login'

# Email configs
EMAIL_BACKEND = env.str('DJANGO_D_APP_EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')
EMAIL_HOST = env.str('DJANGO_D_APP_EMAIL_HOST', default='smtp.server.com')
EMAIL_USE_TLS = env.bool('DJANGO_D_APP_EMAIL_USE_TLS', default=True)
EMAIL_PORT = env.int('DJANGO_D_APP_EMAIL_PORT', default=587)
EMAIL_HOST_USER = str(env('DJANGO_D_APP_EMAIL_USER', default='default@app.com'))
EMAIL_HOST_PASSWORD = str(env('DJANGO_D_APP_EMAIL_PASSWORD', default='passwordEMAIL'))
