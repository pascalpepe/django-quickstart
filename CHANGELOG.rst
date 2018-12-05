=========
Changelog
=========

{% comment %}

Version 1.1
===========

*2018-12-05*

Changed
-------

* Renamed version-related variables from "dunder" format to constant variables.

----

Version 1.0
===========

*2018-12-02*

Supported Django and Python versions
------------------------------------

======== =============
Django   Python
======== =============
1.11 LTS 3.4, 3.5, 3.6
======== =============

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
* **tox** configuration for testing the project and the docs, and running code
  quality checks with **flake8**.
* **GitLab CI** configuration.

{% endcomment %}
