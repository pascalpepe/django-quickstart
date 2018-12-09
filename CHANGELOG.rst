=========
Changelog
=========

{% comment "Content of this block will be ignored when starting your project." %}

Latest
======

* Change max line length to 99.
* Change comment block message in ``README.rst`` and ``CHANGELOG.rst``
* Add status badges in ``README.rst``.

Version 1.2
===========

*2018-12-07*

Changed
-------

* Use a single requirements file.

----

Version 1.1
===========

*2018-12-05*

Added
-----

* Added paths to static and templates directories in common settings.

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
