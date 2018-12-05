=========
Changelog
=========

{% comment %}

Version 2.1
===========

*2018-12-05*

Supported Django and Python versions
------------------------------------

* Support for Django 1.11 LTS is now carried out through the branch
  `stable/1.1.x <https://gitlab.com/padjana/padjana-start-django/tree/stable/1.1.x>`_.
* The compatibility table is now:

  ==================== ======== =============
  Padjana Start Django Django   Python
  ==================== ======== =============
  1.1                  1.11 LTS 3.4, 3.5, 3.6
  -------------------- -------- -------------
  2.1                  2.1      3.5, 3.6, 3.7
  ==================== ======== =============

Added
-----

* Added paths to static and templates directories in common settings.

Changed
-------

* Renamed version-related variables from "dunder" format to constant variables.

----

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
  `stable/1.0.x <https://gitlab.com/padjana/padjana-start-django/tree/stable/1.0.x>`_.
* The compatibility table is now:

  ==================== ======== =============
  Padjana Start Django Django   Python
  ==================== ======== =============
  1.0                  1.11 LTS 3.4, 3.5, 3.6
  -------------------- -------- -------------
  2.0                  2.1      3.5, 3.6, 3.7
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
* Different settings for multiple deployment environments (e.g. development,
  production).
* Ready for internationalization.
* Settings for sending email.
* Error reporting and logging.
* Storage and deployment of static files (assuming that static files are served
  from the same server as the site).
* Enforced site-wide HTTPS in production environment.
* **Sphinx** documentation initialized with a changelog file and using the
  theme sphinx-rtd-theme.
* Code quality checks with **flake8**.
* Automated testing with **tox**.
* **GitLab CI** configuration.

{% endcomment %}
