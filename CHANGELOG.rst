=========
Changelog
=========

{% comment %}

Version 2.0
===========

*2018-12-02*

Supported Django and Python versions
------------------------------------

* Starting from this release, the template is compatible with Django 2.1 only.
* Consequently,

    - support for Python 3.4 is dropped,
    - Python 3.7 is now supported.

* Support for Django 1.11 LTS is now carried out through the branch
  `stable/1.0.x <https://gitlab.com/padjana/open-source/padjana-start-django/tree/stable/1.0.x>`_.
* The compatibility table is now:

  ==================== ======== =============
  Padjana Start Django Django   Python
  ==================== ======== =============
  2.0                  2.1      3.5, 3.6, 3.7
  -------------------- -------- -------------
  1.0                  1.11 LTS 3.4, 3.5, 3.6
  ==================== ======== =============

Changed
-------

* Use new ``path`` function instead of ``url`` in URL configuration.
* **tox** and **GitLab CI** configuration files have been changed to reflect
  the changes in supported Python versions, as detailed above.

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
