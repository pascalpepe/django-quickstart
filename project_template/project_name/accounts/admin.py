"""Admin site configuration for {{ project_name|capfirst }} Accounts."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from {{ project_name }}.accounts.models import User


admin.site.register(User, UserAdmin)
