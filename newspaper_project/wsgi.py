"""
WSGI config for newspaper_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newspaper_project.settings.dev')

application = get_wsgi_application()
