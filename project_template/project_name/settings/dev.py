"""Development settings for {{ project_name|capfirst }}.

Unsuitable for production.
"""

import os

from .base import *  # noqa


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'not-safe-for-prod')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),  # noqa
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/{{ docs_version }}/howto/static-files/

DATA_DIR = os.path.join(BASE_DIR, '.local')  # noqa

MEDIA_ROOT = os.path.join(DATA_DIR, 'media')

STATIC_ROOT = os.path.join(DATA_DIR, 'static')


# Sending email
# https://docs.djangoproject.com/en/{{ docs_version }}/topics/email/

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
