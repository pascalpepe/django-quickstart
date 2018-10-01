"""
Django development settings for {{ project_name }} project.

Quick-start development settings - unsuitable for production

Before deploying your Django project, see
https://docs.djangoproject.com/en/{{ docs_version }}/howto/deployment/checklist/
"""

import os

from .common import *  # noqa


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', '{{ secret_key }}')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Sending email
# https://docs.djangoproject.com/en/{{ docs_version }}/topics/email/

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
