=======================
Quick Start with Django
=======================

.. image:: https://img.shields.io/badge/django-2.2-0c4b33.svg
   :alt: Django 2.2
   :target: https://gitlab.com/pascalpepe/django-quickstart

.. image:: https://img.shields.io/badge/python-3.5%20|%203.6%20|%203.7%20|%203.8-3776ab.svg
   :alt: Python 3.5, 3.6, 3.7, 3.8
   :target: https://gitlab.com/pascalpepe/django-quickstart

.. image:: https://img.shields.io/badge/license-MIT-green.svg
   :alt: MIT License
   :target: https://gitlab.com/pascalpepe/django-quickstart/blob/master/LICENSE

Project template for a quick start with the Django_ framework.

:Source code: https://gitlab.com/pascalpepe/django-quickstart
:Issue tracker: https://gitlab.com/pascalpepe/django-quickstart/issues


Overview
========

This repository provides yet another project template that aims at taking care
of the necessary boilerplate when starting a new Django project. It is
obviously more opinionated than the one included in Django, but hopefully not
too much.

By using this template, you will start with a project for which:

* Django settings are split into environment-specific modules.
* Sensitive settings (e.g. secret key, database password) are loaded from
  environment variables.
* A custom user model is already set up. It behaves identically to the default
  user model, but this makes it easier to customize it mid-project if needed.
  For more information, refer to the official documentation on
  `using a custom user model when starting a project`_.
* PostgreSQL is set as the default database engine in production.
* The paths to project-level templates and static files are set.
* Error pages can be browsed during development.
* Emails are sent with the `console backend`_ during development.

Additionally, this project template includes some commonly used tools for
testing and linting:

* Tests are automated with tox_.
* Code coverage is measured with `coverage.py`_.
* Linting is performed with flake8_.
* `django-debug-toolbar`_ is installed and already set up during development.
* A minimal configuration file for `GitLab CI`_ is provided.


Supported versions of Django and Python
=======================================

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

1. `Install Django 2.2`_ (preferably within a `Python virtual environment`_).

2. Get the project template::

     git clone https://gitlab.com/pascalpepe/django-quickstart.git

3. Start a new Django project (replace the project ``name`` and its optional
   destination ``directory`` as you see fit)::

     django-admin startproject name [directory] --template ./django-quickstart/project_template/ --extension py,rst,txt

   For more information, refer to the official documentation on
   `using the startproject command`_.

4. Initialize your database::

     python manage.py makemigrations
     python manage.py migrate

5. You are all set and ready to start working on your new project::

     python manage.py runserver


Changelog
=========

All changes in this repository are logged in the file `CHANGELOG.rst`_.


License
=======

This project is licensed under the `MIT License`_.


.. _Django: https://www.djangoproject.com
.. _`using a custom user model when starting a project`: https://docs.djangoproject.com/en/2.2/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project
.. _`console backend`: https://docs.djangoproject.com/en/2.2/topics/email/#console-backend
.. _tox: https://tox.readthedocs.io
.. _`coverage.py`: https://coverage.readthedocs.io
.. _flake8: https://flake8.readthedocs.io
.. _`django-debug_toolbar`: https://django-debug-toolbar.readthedocs.io
.. _`GitLab CI`: https://docs.gitlab.com/ee/ci/README.html
.. _`Install Django 2.2`: https://docs.djangoproject.com/en/2.2/topics/install/
.. _`Python virtual environment`: https://docs.python.org/3/library/venv.html
.. _`using the startproject command`: https://docs.djangoproject.com/en/2.2/ref/django-admin/#startproject
.. _CHANGELOG.rst: https://gitlab.com/pascalpepe/django-quickstart/blob/master/CHANGELOG.rst
.. _`MIT License`: https://gitlab.com/pascalpepe/django-quickstart/blob/master/LICENSE
