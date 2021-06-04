About PostgreSQL Disk Usage
=============================

When you create your first Aiven for PostgreSQL service, you may see the disk usage gradually increasing even though you are not yet inserting or updating much data.

.. image:: pictures/d3d3bc6c73d18c5b2cbf0985_image.png

This is completely normal within the first 24 hours of operation for Aiven PostgreSQL services because of our WAL (Write-Ahead Logging) archiving settings.

To prevent loss of data due to node failure on Hobbyist and Startup plans, we set the ``archive_timeout`` configuration to write WAL segments to disk at regular intervals. The WAL segments are then backed up to cloud storage. Even if your service is idle, each WAL segment occupies the same amount of space on disk, which is why the disk usage grows steadily over time.

After the first 24 hours of service, the system begins archiving old WAL segments and deleting them from disk to free up space. From this point onward, new WAL segments no longer have such a high impact on disk usage as the service reaches a steady state for low-traffic services.

You can read more about WAL archiving `in the PostgreSQL manual <https://www.postgresql.org/docs/current/runtime-config-wal.html#RUNTIME-CONFIG-WAL-ARCHIVING>`_.
