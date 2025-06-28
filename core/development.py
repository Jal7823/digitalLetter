# core/settings/development.py

from .base import *

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Configuración para base de datos local, si quieres distinta
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Otros settings específicos para desarrollo, ej:
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
