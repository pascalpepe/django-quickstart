"""Models for {{ project_name|capfirst }} Accounts."""

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Model representing a user."""
