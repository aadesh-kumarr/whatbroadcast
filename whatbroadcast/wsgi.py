"""
WSGI config for whatbroadcast project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
import whatbroadcast
import gunicorn

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'whatbroadcast.settings')

application = get_wsgi_application()

app=application
gunicorn whatbroadcast.wsgi:application --bind 0.0.0.0:$PORT
