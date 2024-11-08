"""
WSGI config for reviews_book_hw project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

# requerements.txt - gunicorn, django, dj
# wsgi - reviews_book.settings'
# settings - allowed hosts

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'reviews_book.settings')

application = get_wsgi_application()
