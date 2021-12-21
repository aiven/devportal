Estimate maximum number of connection in Aiven for Redis
========================================================

The number of simultaneous connections in Aiven for Redis depends on the total available memory on the server. 


Here is how you can estimate it:

.. math::

   4\times m

where `m` represents the memory in megabytes (MB) binary. With at least 10000 connections available, even on the smallest servers. For example, on a server with 4GB memory (4,096 MB binary), the simultaneous connections are:

.. math::

    4\times 4096 = 16384 

.. note::

    Make sure to convert the memory unit to MB binary unit

Learn more about `Aiven for Redis <https://aiven.io/redis>`_ and how its managed.