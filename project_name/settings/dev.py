"""
Development settings for {{ project_name }} project.

Quick-start development settings - unsuitable for production

Before deploying your Django project, see
https://docs.djangoproject.com/en/{{ docs_version }}/howto/deployment/checklist/
"""

import os

from .base import *  # noqa


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '{{ secret_key }}'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DATABASE_NAME', ''),
        'USER': os.environ.get('DATABASE_USER', ''),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', ''),
        'HOST': os.environ.get('DATABASE_HOST', ''),
        'PORT': os.environ.get('DATABASE_PORT', '5432'),
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

DATA_DIR = os.path.join(BASE_DIR, '.local')  # noqa

MEDIA_ROOT = os.path.join(DATA_DIR, 'media')

STATIC_ROOT = os.path.join(DATA_DIR, 'static')


# Sending email
# https://docs.djangoproject.com/en/{{ docs_version }}/topics/email/

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
