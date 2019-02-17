"""
Production settings for {{ project_name }} project.

Before deploying your Django project, see
https://docs.djangoproject.com/en/{{ docs_version }}/howto/deployment/checklist/
"""

from .common import *  # noqa


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'keepItSecret!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['.domain.tld']


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '5432',
    }
}


# Sending email
# https://docs.djangoproject.com/en/{{ docs_version }}/topics/email/

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# EMAIL_HOST_USER = ''
#
# EMAIL_HOST_PASSWORD = ''
#
# EMAIL_HOST = ''
#
# EMAIL_PORT = 587
#
# EMAIL_USE_TLS = True


# SSL/HTTPS
# https://docs.djangoproject.com/en/{{ docs_version }}/topics/security/#ssl-https

SECURE_SSL_REDIRECT = True

CSRF_COOKIE_SECURE = True

SESSION_COOKIE_SECURE = True
