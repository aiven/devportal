Handle page redirects
=====================

Devportal uses the filename to define the page url, so for example the page
``docs/platform/concepts/database-forking.rst``
will be available as https://developer.aiven.io/docs/platform/concepts/database-forking.html

Sometimes you'll need to

* Change the page name to be more representative of the content
* Remove the content from a page because is no longer relevant

However, this can make search indexes unhappy, and it is also possible that other locations were linking to the original page. Therefore when renaming or removing a page, you should keep the original, but change its content to make it into a redirect.

For example `PR #710 <https://github.com/aiven/devportal/pull/710>`__ wanted to rename the page ``database-forking.rst`` to ``service-forking.rst``

This was done by renaming the original page (and adjusting the ``_toc.yml`` file), and then creating a new ``database-forking.rst`` page with the following content:

.. code:: reStructuredText

    :orphan:

    .. raw:: html

        <script type="text/javascript">
            window.location.replace('/docs/platform/concepts/service-forking.html');
        </script>

    This page is a redirect from ``database-forking`` to ``service-forking``, since the original name (``database-forking``) was incorrect.
    It's part of `PR #710 <https://github.com/aiven/devportal/pull/710>`_

The ``:orphan:`` section tells sphinx not to include this page in any contents list, which means that it does not issue a warning that ``database-forking.rst`` isn't included in the ``_toc.yaml`` file.

The javascript inside the ``.. raw:: html`` does the redirect.
