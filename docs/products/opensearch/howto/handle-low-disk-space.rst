Handle low disk space
======================

When you're running low on disk space using Aiven OpenSearch, you can take one of these actions:

-  Upgrade to a larger plan from with a help of `Aiven console <https://console.aiven.io/>`_ or by using `Aiven CLI client <https://github.com/aiven/aiven-client>`_.

-  Clean up unnecessary indices. Thus, for logs, it is often beneficial to create a separate, daily indices, allowing easy and efficient clean-up of the oldest data.


Mechanisms to handle low disk space
-----------------------------------

OpenSearch relies on three indicators to identify and respond to low disk space.

Disk allocation low watermark
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Defined by parameter ``cluster.routing.allocation.disk.watermark.low`` and the default value is set to 85% of the disk space.

When this limit is exceeded, OpenSearch starts avoiding allocating new shards to the server. On a single-server OpenSearch, this has no effect. On a multi-server cluster, amount of data is not always equally distributed, in which case this will help balancing disk usage between servers.

Disk allocation high watermark
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Defined by parameter ``cluster.routing.allocation.disk.watermark.high`` and the default value is set to 90% of the disk space.

When this limit is exceeded, OpenSearch will actively try to move shards to other servers with more available disk space. On  a single-server OpenSearch, this has no effect.

Disk allocation flood stage watermark
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Defined by parameter ``cluster.routing.allocation.disk.watermark.flood_stage`` and the default value is set to 95% of the disk space.

When this limit is exceeded, OpenSearch will mark all indices hosted on the server exceeding this limit as read-only, allowing deletes (``index.blocks.read_only_allow_delete``).

Mechanisms to handle low disk space
-----------------------------------

If ``low`` or ``high`` watermark thresholds are exceeded, but data is eventually cleaned up, no further action is needed, as OpenSearch will continue allowing writes. However, if ``flood_state`` is exceeded, **you must manually unset** ``read_only_allow_delete`` **for each affected index**. This can be done by updating index settings:

.. code::

    curl https://avnadmin:your-password@your-server-demoprj.aivencloud.com:port/indexname/_settings -X PUT -H 'Content-Type: application/json' -d '{"index.blocks.read_only_allow_delete": null}'

.. note::

    This needs to be done separately for each index that was marked as read-only by OpenSearch.

.. note::

    Aiven does not automatically unset this option to ensure no flipping around read-only and read-write state.
