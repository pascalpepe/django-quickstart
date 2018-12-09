{% comment "Content of this block will be ignored when starting your project." %}

============================
Padjana Start Django Project
============================

Project template for a quick start with Django framework.

Status
======

.. image:: https://img.shields.io/badge/django-1.11-blue.svg
    :alt: django versions
    :target: https://gitlab.com/padjana/padjana-startproject

.. image:: https://img.shields.io/badge/python-3.4%20%7C%203.5%20%7C%203.6-blue.svg
    :alt: python versions
    :target: https://gitlab.com/padjana/padjana-startproject

.. image:: https://img.shields.io/badge/license-MIT-yellowgreen.svg
    :alt: MIT license
    :target: https://choosealicense.com/licenses/mit/

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

======== =============
Django   Python
======== =============
1.11 LTS 3.4, 3.5, 3.6
======== =============

It is recommended that you install the latest patch/minor releases (A.B.C)
available for your system.

Usage
=====

`Install Django 1.11 <https://docs.djangoproject.com/en/1.11/topics/install/>`_
and run the following command::

    django-admin startproject name [directory] --template https://gitlab.com/padjana/padjana-startproject/-/archive/support/django111/padjana-startproject-support-django111.zip --extension py,rst,txt

For more information on the ``startproject`` command, see
https://docs.djangoproject.com/en/1.11/ref/django-admin/#startproject

About Padjana
=============

**Padjana** offers free and open-source software built with and for the
**Django** framework.

All Django applications developed by Padjana follow the same guidelines and
design philosophy. For more information, visit https://www.padjana.com.

License
=======

This project is licensed under the MIT License.
`Learn more <https://choosealicense.com/licenses/mit/>`_.

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

It is recommended that you install the latest patch/minor releases (A.B.C)
available for your system.
