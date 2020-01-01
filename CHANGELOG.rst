=========
Changelog
=========

{% comment "Content of this block will be ignored when starting your project." %}

Version 3.1
===========

In development.

* Updated psycopg2-binary to version 2.8.4.
* Moved flake8 config from ``setup.cfg`` to ``tox.ini``.
* Renamed ̀``settings/common.py`` as ``settings/base.py``.
* Removed the empty Sphinx docs.
* Moved local static files to:

  - ``/.local/`` during development (the directory is ignored by version
    control).
  - a ``DATA_DIR`` environment variable in production.

* Moved project-level templates, static files and locale files to the root
  directory.
* Added custom pages for the following errors:

  - 400 Bad Request
  - 403 Forbidden
  - 404 Not Found
  - 500 Internal Server Error

* Added URL paths so as to be able to browse error pages during development.
* Added URL path to serve files uploaded by users (i.e. ``/.local/media/``)
  during development

----

Version 3.0
===========

2019-04-06

Supported Django and Python versions
------------------------------------

* Starting from this release, the template is compatible with Django 2.2 only.
* Support for Django 1.11 (old LTS) and Django 2.1 is dropped.
* The compatibility table is now:

  ================= ======== =============
  Branch            Django   Python
  ================= ======== =============
  master            2.2      3.5, 3.6, 3.7
  ================= ======== =============

Changed
-------

* Fixed the docs version in settings. Some docstrings were written with "2.1"
  instead of the template variable.
* Changed the ``SERVER_EMAIL`` setting to ``no-reply@`` instead of ``root@``.
* Uncommented the email settings in the production settings example.
* Changed the default database host in the production settings example to
  ``127.0.0.1`` instead of an empty string.
* Updated ``README.rst`` to reflect the Django upgrade.

----

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
