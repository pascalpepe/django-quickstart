"""Views for {{ project_name|capfirst }} Home."""

from django.views.generic.base import TemplateView


class Home(TemplateView):
    """View that displays the home page."""

    template_name = 'home/home.html'
    extra_context = {
        'version': '{{ docs_version }}',
    }
