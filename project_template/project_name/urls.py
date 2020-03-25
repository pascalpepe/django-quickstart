"""URL configuration for {{ project_name|capfirst }}.

The ``urlpatterns`` list routes URLs to views.

For more information on this file, see:
https://docs.djangoproject.com/en/{{ docs_version }}/topics/http/urls/
"""

from django.conf import settings
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', include('{{ project_name }}.home.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.views import defaults

    import debug_toolbar

    # Make error pages browsable during development
    urlpatterns += [
        path('400/', defaults.bad_request, {'exception': 'Bad Request'}),
        path('403/', defaults.permission_denied, {'exception': 'Forbidden'}),
        path('404/', defaults.page_not_found, {'exception': 'Not Found'}),
        path('500/', defaults.server_error),
    ]
    # Serve files uploaded by a user during development
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    # Add Debug Toolbar's URLs
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
