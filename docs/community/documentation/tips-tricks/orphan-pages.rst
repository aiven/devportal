Create orphan pages
===================

By default any pages created need to be added in the ``_toc.yml`` file and therefore appear in the left navigation section. However you might want to create **orphan** pages which can be linked by other pages but are not present in the main navigation panel. 

To achieve this and avoid build failures, you just need to add the ``:orphan:`` directive in the page like:

.. code:: reStructuredText

    Page title
    ==========

    :orphan:

    Rest of the page content

The ``:orphan:`` section tells Sphinx not to include this page in any contents list, and therefore no warning is issued about the page not being added in the  ``_toc.yaml`` file.
