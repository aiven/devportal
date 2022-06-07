Create anonymous links
======================

If in a page you have multiple links having the same label, for instance:

.. code:: reStructuredText

    `docs <http//docs.com>`_
    `docs <http//docs2.com>`_

You'll see a warning in the logs stating ``Duplicate target name``. To resolve the warning you can either

* change the link labels to be different, or
* create an anonymous link by adding two ``_`` at the end of the link, for instance:

  .. code:: reStructuredText

     `docs <http//docs2.com>`__