=============================
Nobi Child
=============================

.. image:: https://badge.fury.io/py/nobi-child.svg
    :target: https://badge.fury.io/py/nobi-child

.. image:: https://travis-ci.org/nobierp/nobi-child.svg?branch=master
    :target: https://travis-ci.org/nobierp/nobi-child

.. image:: https://codecov.io/gh/nobierp/nobi-child/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/nobierp/nobi-child

Module Child for NobiERP

Documentation
-------------

The full documentation is at https://nobi-child.readthedocs.io.

Quickstart
----------

Install Nobi Child::

    pip install nobi-child

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'nobi_child.apps.NobiChildConfig',
        ...
    )

Add Nobi Child's URL patterns:

.. code-block:: python

    from nobi_child import urls as nobi_child_urls


    urlpatterns = [
        ...
        url(r'^', include(nobi_child_urls)),
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
