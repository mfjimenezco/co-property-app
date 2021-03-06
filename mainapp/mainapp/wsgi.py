"""
WSGI config for mainapp project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mainapp.settings.production')

application = get_wsgi_application()
