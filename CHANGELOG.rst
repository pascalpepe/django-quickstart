=========
Changelog
=========

Latest
======

This release continues the changes in project layout and settings introduced in
version 3.1.

General changes
---------------

* Moved the project template to its own directory: ``project_template/``
* Moved the Accounts application to the project directory.
* Split requirements into environment-specific files.
* Changed imports from relative to absolute everywhere.
* Added a ``NOTICE`` file.
* Updated the following files in accordance with the changes introduced in this
  version: ``.flake8``, ``.gitignore``, ``.gitlab-ci.yml``, ``README``,
  ``tox.ini``.

Settings changes
----------------

* Split the ``INSTALLED_APPS`` into three lists: ``LOCAL_APPS``,
  ``THIRD_PARTY_APPS`` and ``DJANGO_APPS``.
* Changed ``DATA_DIR`` during development from ``.local/`` to ``.data/``.
* Changed the database backend to SQLite3 during development.
* Set ``SERVER_EMAIL`` to ``DEFAULT_FROM_EMAIL``.

New application: Home
---------------------

* Started the Home application.
* Added a minimal template view for the home page.
* Added tests for the home view.

New testing tools
-----------------

* Set up django-debug-toolbar during development.
* Added coverage.py configuration.

Supported versions of Django and Python
---------------------------------------

* Django 2.2.8 added support for Python 3.8. The compatibility table is now:

====== ======= ===================================
Branch Django  Python
====== ======= ===================================
master 2.2 LTS 3.5, 3.6, 3.7, 3.8 (added in 2.2.8)
====== ======= ===================================


Version 3.1
===========

2020-01-01

This update contains many changes in settings and a reorganization of the
project layout.

General changes
---------------

* Moved project-level templates, static files and locale files to the root
  directory.
* Moved flake8 configuration from ``setup.cfg`` to ``tox.ini``.
* Moved collected static files and media files to ``.local/`` during
  development. This directory is ignored by version control. [Renamed as
  ``.data/`` in version 3.2.]

Settings changes
----------------

* Renamed ``settings/common.py`` as ``settings/base.py``.
* Changed sensitive settings in order to be loaded from environment variables
  instead of secret files.
* Moved email-based error-reporting settings to ``settings/prod.py``.
* Changed max line length to 79 (default flake8 value).
* Added a ``DATA_DIR`` constant to indicate the path to ``STATIC_ROOT`` and
  ``MEDIA_ROOT``.

New
---

* Added custom pages for the following errors:

  - 400 Bad Request
  - 403 Forbidden
  - 404 Not Found
  - 500 Internal Server Error

* Added URL paths so as to be able to browse error pages during development.
* Added URL path to serve files uploaded by users during development.

New application: Accounts
-------------------------

It is recommended to use a custom user when starting a project (see
https://docs.djangoproject.com/en/2.2/ref/django-admin/#startproject).

* Started the Accounts application.
* Added a custom user model. It behaves identically to the default user model,
  but this makes it easier to customize it mid-project if needed.

Removed
-------

* Removed the Sphinx docs entirely from the project template, as it contained
  little to no customization from the default ``sphinx-quickstart`` command.

Dependencies updates
--------------------

* Updated psycopg2-binary to version 2.8.4.
* Changed the default Python image to version 3.7 in GitLab CI. Python 3.7 is
  the default version available in Debian stable (10, Buster).


Version 3.0
===========

2019-04-06

Supported versions of Django and Python
---------------------------------------

* Starting from this release, the template is compatible with Django 2.2 only
  (new LTS).
* Support for Django 1.11 (old LTS) and Django 2.1 is dropped.
* The compatibility table is now:

====== ======= =============
Branch Django  Python
====== ======= =============
master 2.2 LTS 3.5, 3.6, 3.7
====== ======= =============

Changed
-------

* Fixed the docs version in settings. Some docstrings were written with "2.1"
  instead of the template variable.
* Changed the ``SERVER_EMAIL`` setting to ``no-reply@`` instead of ``root@``.
* Uncommented all email settings in the production example.
* Changed the default database host in the production example to ``127.0.0.1``
  instead of an empty string.
* Updated ``README.rst`` to reflect the Django upgrade.


Version 2.3
===========

2019-02-17

* Reorganized settings in order to remove most environment variables and use a
  secret file instead.
* Changed GitLab CI configuration to run for all branches instead of only
  master.
* Updated psycopg2-binary to version 2.7.7.
* Changed max line length to 99.
* Changed comment block message in ``README.rst`` and ``CHANGELOG.rst``
* Updated docs requirements file.
* Changed copyright notice in docs configuration so as to use a fixed date.
* Updated ``README.rst`` to reflect most of those changes.


Version 2.2
===========

2018-12-07

* Reorganized the requirements in a single file.


Version 2.1
===========

2018-12-05

* Added paths to static and templates directories in common settings.


Version 2.0
===========

2018-12-02

Supported versions of Django and Python
---------------------------------------

* Starting from this release, the template is compatible with Django 2.1 only.
* Support for Django 1.11 LTS is now carried out through the branch
  ``support/django111``.
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
* Updated tox and GitLab CI configuration files to reflect the changes of
  supported Python versions, as detailed above.


Version 1.0
===========

2018-12-02

Supported versions of Django and Python
---------------------------------------

======== =============
Django   Python
======== =============
1.11 LTS 3.4, 3.5, 3.6
======== =============

Initial features
----------------

* PostgreSQL as default database backend.
* Loading sensitive settings values (e.g. secret key, database password) from
  environment variables.
* Different settings for multiple deployment environments (e.g. development,
  production).
* Ready for internationalization.
* Settings for sending email.
* Error reporting and logging.
* Storage and deployment of static files (assuming that static files are served
  from the same server as the site).
* Enforced site-wide HTTPS in production environment.
* Sphinx documentation initialized with a changelog file and using the
  theme sphinx-rtd-theme.
* Code quality checks with flake8.
* Automated testing with tox.
* GitLab CI configuration.
