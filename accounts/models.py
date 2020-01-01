"""
Models for the accounts application.
"""

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Users within the authentication system are represented by this model.

    This model behaves identically to the default user model, but we will
    be able to customize it in the future if the need arises.
    """

    pass
