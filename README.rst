==================
Django Quick Start
==================

.. image:: https://img.shields.io/badge/django-2.2-blue.svg
    :alt: django versions
    :target: https://gitlab.com/pascalpepe/django-quickstart

.. image:: https://img.shields.io/badge/python-3.5%20%7C%203.6%20%7C%203.7-blue.svg
    :alt: python versions
    :target: https://gitlab.com/pascalpepe/django-quickstart

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :alt: MIT license
    :target: https://gitlab.com/pascalpepe/django-quickstart/blob/master/LICENSE

Project template for a quick start with Django framework.

----

* **Source code**: https://gitlab.com/pascalpepe/django-quickstart
* **Issue tracker**: https://gitlab.com/pascalpepe/django-quickstart/issues

----

Project template overview
=========================

* Django settings are split into environment-specific modules (e.g.
  development, staging, production).
* Sensitive settings (e.g. secret key, database password) are loaded from
  environment variables.
* PostgreSQL is set as the default database engine in production.
* A custom user model is already set up (it behaves identically to the default
  user model).
* Code quality checks with **flake8**.
* Automated testing with **tox**.
* Continuous integration with **GitLab CI**.


Supported Django and Python versions
====================================

This project aims at supporting the latest LTS version of Django.

======= ===================================
Django  Python
======= ===================================
2.2 LTS 3.5, 3.6, 3.7, 3.8 (added in 2.2.8)
======= ===================================

For each version of Python, it is recommended that you install the latest
micro release (A.B.C) available on your system.

For Django, the latest LTS micro release (2.2.x) is recommended.


Quick usage guide
=================

1. `Install Django 2.2 <https://docs.djangoproject.com/en/2.2/topics/install/>`_
   (preferably within a Python 3 virtual environment).

2. Get the project template::

     git clone https://gitlab.com/pascalpepe/django-quickstart.git

3. Start a new Django project (replace the project ``name`` and its optional
   destination ``directory`` as you see fit)::

     django-admin startproject name [directory] --template ./django-quickstart/project_template/ --extension py,rst,txt

   For more information on the ``startproject`` command, see https://docs.djangoproject.com/en/2.2/ref/django-admin/#startproject

4. Initialize your database::

     python manage.py makemigrations
     python manage.py migrate

5. You are all set and ready to start working on your new project::

     python manage.py runserver


License
=======

This project is licensed under the `MIT License <https://gitlab.com/pascalpepe/django-quickstart/blob/master/LICENSE>`_.
