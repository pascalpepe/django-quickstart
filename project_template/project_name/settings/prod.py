"""Production settings for {{ project_name|capfirst }}.

Before deploying, see
https://docs.djangoproject.com/en/{{ docs_version }}/howto/deployment/checklist/
"""

import os

from .base import *  # noqa


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    '.domain.tld',
]


# Database
# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DATABASE_NAME', ''),
        'USER': os.environ.get('DATABASE_USER', ''),
        'PASSWORD': os.environ['DATABASE_PASSWORD'],
        'HOST': os.environ.get('DATABASE_HOST', '127.0.0.1'),
        'PORT': os.environ.get('DATABASE_PORT', '5432'),
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/{{ docs_version }}/howto/static-files/

DATA_DIR = os.environ['DATA_DIR']

MEDIA_ROOT = os.path.join(DATA_DIR, 'media')

STATIC_ROOT = os.path.join(DATA_DIR, 'static')

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'  # noqa


# Sending email
# https://docs.djangoproject.com/en/{{ docs_version }}/topics/email/

DEFAULT_FROM_EMAIL = 'no-reply@domain.tld'

EMAIL_HOST = os.environ.get('EMAIL_HOST', ''),

EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', ''),

EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']


# Error reporting
# https://docs.djangoproject.com/en/{{ docs_version }}/howto/error-reporting/

ADMINS = [
    ('Jane Smith', 'jane.smith@domain.tld'),
    ('John Smith', 'john.smith@domain.tld'),
]

SERVER_EMAIL = 'no-reply@domain.tld'


# Security
# https://docs.djangoproject.com/en/{{ docs_version }}/topics/security/

CSRF_COOKIE_HTTPONLY = True

CSRF_COOKIE_SECURE = True

SESSION_COOKIE_SECURE = True
