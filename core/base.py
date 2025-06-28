# core/settings/base.py

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = 'tu-secreto-aqui'  # Idealmente leerlo de variable de entorno

INSTALLED_APPS = [
    # apps Django
    'django.contrib.admin',
    'django.contrib.auth',
    # ...
    # apps propias
    'apps.users',
    'apps.products',
    'apps.categories',
    'apps.company',
    # librerías externas
    'rest_framework',
    'drf_spectacular',
    # etc...
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # ...
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    # ...
]

WSGI_APPLICATION = 'core.wsgi.application'

# Aquí puedes poner configuración por defecto de base de datos, si quieres:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Rest Framework, Internacionalización, Static/Media, etc

# Por ejemplo:
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

# Static files
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# Y otras configuraciones comunes...
