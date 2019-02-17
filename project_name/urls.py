"""
URL configuration for {{ project_name }} project.

The `urlpatterns` list routes URLs to views.

For more information on this file, see:
https://docs.djangoproject.com/en/{{ docs_version }}/topics/http/urls/

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function:  from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
]

# Internationalization
# https://docs.djangoproject.com/en/{{ docs_version }}/topics/i18n/
# from django.conf.urls.i18n import i18n_patterns
# from django.utils.translation import gettext_lazy as _
# urlpatterns += i18n_patterns()

# Serve files uploaded by users during development
# https://docs.djangoproject.com/en/{{ docs_version }}/howto/static-files/
# from django.conf import settings
# from django.conf.urls.static import static
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
