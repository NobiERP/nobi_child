=====
Usage
=====

To use Nobi Family in a project, add it to your `INSTALLED_APPS`:

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
