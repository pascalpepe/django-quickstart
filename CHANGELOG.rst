=========
Changelog
=========

{% comment %}

Version 2.0
===========

*2018-12-01*

Supported Django and Python versions
------------------------------------

====== =============
Django Python
====== =============
2.1    3.5, 3.6, 3.7
====== =============

Initial features
----------------

* **PostgreSQL** as default database backend.
* Loading sensible settings values (e.g. secret key, database password) from
  environment variables.
* Different settings and requirements for multiple deployment environments
  (e.g. development, production).
* Project translatable from the get-go.
* Sending email (using the console backend for development and the SMTP backend
  for production).
* Error reporting and logging.
* Storage and deployment of static files (assuming that static files are served
  from the same server as the site).
* Site-wide HTTPS in production environment.
* **Sphinx** documentation with the theme **sphinx-rtd-theme**.
* **tox** configuration for testing the project, docs build and code quality
  (with **flake8**).
* **GitLab CI** configuration. All jobs are hidden and need to be activated
  when the project is ready.

{% endcomment %}
