"""
Django production settings for {{ project_name }} project.

Before deploying your Django project, see
https://docs.djangoproject.com/en/{{ docs_version }}/howto/deployment/checklist/
"""

import os

from .common import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = os.environ['ALLOWED_HOSTS'].split(',')


# Sending email
# https://docs.djangoproject.com/en/{{ docs_version }}/topics/email/

EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']

EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']

EMAIL_HOST = os.environ['EMAIL_HOST']

EMAIL_PORT = 587

EMAIL_USE_TLS = True


# SSL/HTTPS
# https://docs.djangoproject.com/en/{{ docs_version }}/topics/security/#ssl-https

SECURE_SSL_REDIRECT = True

CSRF_COOKIE_SECURE = True

SESSION_COOKIE_SECURE = True
