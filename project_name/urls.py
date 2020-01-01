"""
URL configuration for {{ project_name }} project.

The `urlpatterns` list routes URLs to views.

For more information on this file, see:
https://docs.djangoproject.com/en/{{ docs_version }}/topics/http/urls/
"""

from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views


urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
)

if settings.DEBUG:
    # Browse custom error pages during development
    urlpatterns += i18n_patterns(
        path(
            '400/',
            default_views.bad_request,
            kwargs={'exception': Exception('Bad Request')},
        ),
        path(
            '403/',
            default_views.permission_denied,
            kwargs={'exception': Exception('Forbidden')},
        ),
        path(
            '404/',
            default_views.page_not_found,
            kwargs={'exception': Exception('Not Found')},
        ),
        path(
            '500/',
            default_views.server_error,
        ),
    )
    # Serve files uploaded by users during development
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
