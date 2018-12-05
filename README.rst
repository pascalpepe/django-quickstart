{% comment %}

============================
Padjana Start Django Project
============================

Project template for a quick start with Django framework.

Features
========

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

Supported Django and Python versions
====================================

==================== ======== =============
Padjana Start Django Django   Python
==================== ======== =============
1.1                  1.11 LTS 3.4, 3.5, 3.6
-------------------- -------- -------------
2.1                  2.1      3.5, 3.6, 3.7
==================== ======== =============

It is recommended that you install the latest minor releases (A.B.C) available
for your system.

Usage
=====

`Install Django 1.11 <https://docs.djangoproject.com/en/1.11/topics/install/>`_
and run the following command::

    django-admin startproject name [directory] --template https://gitlab.com/padjana/padjana-start-django/-/archive/stable/1.1.x/padjana-start-django-stable-1.1.x.zip --extension py,rst,txt

For more information on the ``startproject`` command, see
https://docs.djangoproject.com/en/1.11/ref/django-admin/#startproject

About Padjana
=============

**Padjana** offers a set of open-source projects, applications and tools
developed with and for **Django**, all following the same guidelines and
striving to be compatible with each other.

Unless noted otherwise, each Django application developed by Padjana can be
used individually and included seamlessly within existing Django projects.

For more information, visit https://www.padjana.com.

License
=======

This project is licensed under the
`MIT License <https://gitlab.com/padjana/padjana-startapp-django/blob/master/LICENSE>`_.

{% endcomment %}

==================
{{ project_name }}
==================

Supported Django and Python versions
====================================

======== =============
Django   Python
======== =============
1.11 LTS 3.4, 3.5, 3.6
======== =============

It is recommended that you install the latest minor releases (A.B.C) available
for your system.
