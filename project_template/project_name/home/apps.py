"""Configuration for {{ project_name|capfirst }} Home."""

from django.apps import AppConfig


class HomeConfig(AppConfig):
    """Home application configuration."""

    name = '{{ project_name }}.home'
