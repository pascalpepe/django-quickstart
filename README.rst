{% comment "Content of this block will be ignored when starting your project." %}

==================
Django Quick Start
==================

Project template for a quick start with Django framework.


.. image:: https://img.shields.io/badge/django-2.2-blue.svg
    :alt: django versions
    :target: https://gitlab.com/pascalpepe/django-quickstart

.. image:: https://img.shields.io/badge/python-3.5%20%7C%203.6%20%7C%203.7-blue.svg
    :alt: python versions
    :target: https://gitlab.com/pascalpepe/django-quickstart

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :alt: MIT license
    :target: https://gitlab.com/pascalpepe/django-quickstart/blob/master/LICENSE

----

* **Source code**: https://gitlab.com/pascalpepe/django-quickstart
* **Issue tracker**: https://gitlab.com/pascalpepe/django-quickstart/issues

----

Features
========

* **PostgreSQL** as default database engine.
* Sensible settings (e.g. secret key, database password) loaded from
  environment variables.
* Split settings for multiple deployment environments (e.g. development,
  staging, production).
* Ready for internationalization.
* Custom user model set from the start (identical to the default user model).
* Storage and deployment of static files (assuming that static files are served
  from the same server as the site).
* Enforced site-wide HTTPS in a production environment.
* Settings for error reporting.
* Code quality checks with **flake8**.
* Automated testing with **tox**.
* Continuous integration with **GitLab CI**.

Supported Django and Python versions
====================================

This project aims at supporting the latest LTS version of Django.

======== =============
Django   Python
======== =============
2.2 LTS  3.5, 3.6, 3.7
======== =============

It is recommended that you install the latest patch/minor releases (A.B.C)
available on your system for both Django and Python.

Usage
=====

1. `Install Django 2.2 <https://docs.djangoproject.com/en/2.2/topics/install/>`_
   (preferably within a Python 3 virtual environment).
2. Start a new Django project (replace the project ``name`` and its optional
   destination ``directory`` as you see fit)::

     django-admin startproject name [directory] --template https://gitlab.com/pascalpepe/django-quickstart/-/archive/master/django-quickstart-master.zip --extension py,rst,txt

   For more information on the ``startproject`` command, see https://docs.djangoproject.com/en/2.2/ref/django-admin/#startproject
3. Configure your project:

   * Set ``TIME_ZONE`` to your time zone in ``settings/base.py``.
   * Set your database credentials with environment variables as defined in
     ``settings/dev.py``.

4. Initialize your database::

     python manage.py makemigrations accounts
     python manage.py migrate

5. You are all set and ready to work on your new project.

License
=======

This project is licensed under the `MIT License <https://gitlab.com/pascalpepe/django-quickstart/blob/master/LICENSE>`_.

{% endcomment %}
