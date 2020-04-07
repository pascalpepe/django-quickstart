"""Tests for {{ project_name|capfirst }} Home."""

from django.test import SimpleTestCase
from django.urls import reverse


class HomeViewTest(SimpleTestCase):
    """Tests for the home view."""

    def test_route_from_name(self):
        """The home view is accessible by name."""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_route_from_path(self):
        """The home view is accessible by path."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_templates_used(self):
        """The home view uses the correct templates."""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/home.html')
        self.assertTemplateUsed(response, 'base.html')
