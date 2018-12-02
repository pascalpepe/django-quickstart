{% comment %}

====================
Padjana Start Django
====================

Project template for a quick start with Django framework.

About Padjana for Django
========================

**Padjana for Django** is a set of tools and applications developed with and
for the widely-acclaimed Web framework. All projects follow the same
guidelines and strive to be compatible with each other. Unless noted
otherwise, each application may very well be used individually and included
within existing Django projects.

For more information, visit https://www.padjana.com/open-source/.

Features
========

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

Supported Django and Python versions
====================================

==================== ======== =============
Padjana Start Django Django   Python
==================== ======== =============
2.0                  2.1      3.5, 3.6, 3.7
-------------------- -------- -------------
1.0                  1.11 LTS 3.4, 3.5, 3.6
==================== ======== =============

It is recommended that you install the latest minor releases (A.B.C) available
for your system.

How to use
==========

If you intend to start your project with Django 1.11 LTS, please refer to the
`version 1.0 <https://gitlab.com/padjana/open-source/padjana-start-django/tree/stable/1.0.x>`_.
of this template.

`Install Django <https://docs.djangoproject.com/en/2.1/topics/install/>`_ and
run the following command::

    django-admin startproject name [directory] --template https://gitlab.com/padjana/open-source/padjana-start-django/-/archive/master/padjana-start-django-master.zip --extension py,rst,txt

For more information on the ``startproject`` command, see
https://docs.djangoproject.com/en/2.1/ref/django-admin/#startproject

License
=======

This project is licensed under the `MIT License <https://gitlab.com/padjana/open-source/padjana-startapp-django/blob/master/LICENSE>`_.

{% endcomment %}

==================
{{ project_name }}
==================

Supported Django and Python versions
====================================

====== =============
Django Python
====== =============
2.1    3.5, 3.6, 3.7
====== =============

It is recommended that you install the latest minor releases (A.B.C) available
for your system.
