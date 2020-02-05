=====
Usage
=====

To use Nobi Child in a project, add it to your `INSTALLED_APPS`:

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
