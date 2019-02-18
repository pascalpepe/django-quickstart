=========
Changelog
=========

{% comment "Content of this block will be ignored when starting your project." %}

Version 1.3
===========

2019-02-18

* Reorganized settings in order to remove most environment variables and use a
  secret file instead.
* Changed GitLab CI configuration to run for all branches instead of only
  master.
* Upgraded psycopg2-binary to version 2.7.7.
* Changed max line length to 99.
* Changed comment block message in README.rst and CHANGELOG.rst
* Updated docs requirements file.
* Changed copyright notice in docs configuration so as to use a fixed date.
* Updated README.rst to reflect most of those changes.

----

Version 1.2
===========

2018-12-07

Changed
-------

* Reorganized the requirements in a single file.

----

Version 1.1
===========

2018-12-05

Added
-----

* Added paths to static and templates directories in common settings.

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

* **PostgreSQL** as default database engine.
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
