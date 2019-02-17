=========
Changelog
=========

{% comment "Content of this block will be ignored when starting your project." %}

Version 2.3
===========

2019-02-17

* Reorganized settings in order to remove most environment variables and use a
  secret file instead.
* Changed GitLab CI configuration to run for all branches instead of only
  master.
* Upgraded psycopg2-binary to version 2.7.7.
* Changed max line length to 99.
* Changed comment block message in ``README.rst`` and ``CHANGELOG.rst``
* Updated docs requirements file.
* Changed copyright notice in docs configuration so as to use a fixed date.
* Updated ``README.rst`` to reflect most of those changes.

----

Version 2.2
===========

2018-12-07

* Reorganized the requirements in a single file.

----

Version 2.1
===========

2018-12-05

* Added paths to static and templates directories in common settings.

----

Version 2.0
===========

2018-12-02

Supported Django and Python versions
------------------------------------

* Starting from this release, the template is compatible with Django 2.1 only.
* Support for Django 1.11 LTS is now carried out through the branch
  **support/django111**.
* The compatibility table is now:

  ================= ======== =============
  Branch            Django   Python
  ================= ======== =============
  support/django111 1.11 LTS 3.4, 3.5, 3.6
  ----------------- -------- -------------
  master            2.1      3.5, 3.6, 3.7
  ================= ======== =============

Changed
-------

* Changed the URL configuration to use the new ``path`` function instead of
  ``url``.
* Updated the **tox** and **GitLab CI** configuration files to reflect the
  changes of supported Python versions, as detailed above.

----

Version 1.0
===========

2018-12-02

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
