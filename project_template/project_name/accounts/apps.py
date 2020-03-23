"""Configuration for {{ project_name|capfirst }} Accounts."""

from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """Accounts application configuration."""

    name = '{{ project_name }}.accounts'
