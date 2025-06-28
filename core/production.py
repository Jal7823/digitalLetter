# core/settings/production.py

from .base import *

DEBUG = False

ALLOWED_HOSTS = ['tusitio.com']

# Configuración para base de datos productiva (Postgres, MySQL, etc)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nombre_db',
        'USER': 'usuario',
        'PASSWORD': 'contraseña',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Seguridad
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Variables sensibles como SECRET_KEY deben venir de variables de entorno

# Configuración para servicios externos, almacenamiento, etc
