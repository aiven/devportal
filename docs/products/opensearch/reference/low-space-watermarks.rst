Low disk space watermarks
==========================

OpenSearch® relies on three indicators to identify and respond to low disk space.

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


