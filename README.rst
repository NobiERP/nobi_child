=============================
Nobi Family
=============================

.. image:: https://badge.fury.io/py/nobi-family.svg
    :target: https://badge.fury.io/py/nobi-family

.. image:: https://travis-ci.org/nobierp/nobi-family.svg?branch=master
    :target: https://travis-ci.org/nobierp/nobi-family

.. image:: https://codecov.io/gh/nobierp/nobi-family/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/nobierp/nobi-family

Module Family for NobiERP

Documentation
-------------

The full documentation is at https://nobi-family.readthedocs.io.

Quickstart
----------

Install Nobi Family::

    pip install nobi-family

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'nobi_family.apps.NobiFamilyConfig',
        ...
    )

Add Nobi Family's URL patterns:

.. code-block:: python

    from nobi_family import urls as nobi_family_urls


    urlpatterns = [
        ...
        url(r'^', include(nobi_family_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
