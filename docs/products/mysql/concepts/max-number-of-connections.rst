MySQL max_connections
=====================

The number of simultaneous connections in Aiven for MySQL depends on the :doc:`usable memory </docs/platform/concepts/service-memory-limits>` on the server.

The ``usable memory`` is the total memory on the node minus the operating system and management overhead. This overhead is currently estimated as |vm_overhead|. 

The ``usable memory`` value is then **rounded down to the nearest integer value of GiB**. 

    :math:`⌊usable\_memory⌋ =` |vm_usable_memory|

.. note::
    Independent of the plan, an ``extra_connection`` with a value of ``1`` will be added for the system process.

**For plans under 4 GiB of usable memory**, the number of allowed connections is |mysql_connections_per_<4G| per GiB:

    :math:`{max\_connections} =` |mysql_connections_per_<4G| |mysql_max_connections| 

As an example, with 4 GiB of total memory, the maximum number of connections is:

    :math:`{max\_connections} =` |mysql_connections_per_<4G| :math:`\times {⌊4 -}` |vm_fractional_overhead| :math:`{⌋ +1}`


**For plans higher or equal to 4 GiB**, the number of allowed connections is |mysql_connections_per_>4G| per GiB:
    
    :math:`{max\_connections} =` |mysql_connections_per_>4G| |mysql_max_connections| 

.. include:: /includes/platform-variables.rst