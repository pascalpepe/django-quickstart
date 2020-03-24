"""URL configuration for {{ project_name|capfirst }} Home."""

from django.urls import path

from {{ project_name }}.home import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
]
