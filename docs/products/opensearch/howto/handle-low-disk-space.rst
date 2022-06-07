Handle low disk space
======================

OpenSearch® relies on the watermarks to respond to low disk space. Read more about each of them :doc:`in the dedicated article <../reference/low-space-watermarks>`.

When you're running low on disk space using Aiven for OpenSearch, you can take one of these actions:

-  Upgrade to a larger plan from with a help of `Aiven console <https://console.aiven.io/>`_ or by using `Aiven CLI client <https://github.com/aiven/aiven-client>`_.

-  Clean up unnecessary indices. Thus, for logs, it is often beneficial to create a separate, daily indices, allowing easy and efficient clean-up of the oldest data.

Follow-up actions after cleaning space
---------------------------------------

If ``low watermark`` or ``high watermark`` thresholds are exceeded, but data is eventually cleaned up, no further action is needed, as OpenSearch will continue allowing writes. However, if ``flood_state watermark`` is exceeded, **you must manually unset** ``read_only_allow_delete`` **for each affected index**. This can be done by updating index settings:

.. code::

    curl https://USER:PASSWORD@HOST:PORT/INDEX_NAME/_settings \
    -X PUT \
    -H 'Content-Type: application/json' \
    -d '{"index.blocks.read_only_allow_delete": null}'

These are the placeholders you will need to replace in the code sample:

=========================      =============================================================
Variable                       Description
=========================      =============================================================
``USER``                       User name to use when accessing the OpenSearch cluster
-------------------------      -------------------------------------------------------------
``PASSWORD``                   Password to use when accessing the OpenSearch cluster
-------------------------      -------------------------------------------------------------
``HOST``                       Host name for the connection
-------------------------      -------------------------------------------------------------
``PORT``                       Port number for the connection
-------------------------      -------------------------------------------------------------
``INDEX_NAME``                 Name of the index
=========================      =============================================================

.. warning::

    This needs to be done separately for each index that was marked as read-only by OpenSearch.

.. note::

    Aiven does not automatically unset this option to ensure no flipping around read-only and read-write state.
