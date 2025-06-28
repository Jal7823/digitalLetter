# core/settings/test.py

from .base import *

DEBUG = False

# Base de datos en memoria o separada para tests
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

# Ajustes para tests (ej: menos logs, mail backend dummy, etc)
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]
