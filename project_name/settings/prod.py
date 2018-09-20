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
