Estimate maximum number of connection
=====================================

The number of simultaneous connections in Aiven for Redis™* depends on the total available memory on the server.

You can use the following to estimate:

.. math::

   {max\_number\_of\_connections} = 4\times m

where ``m`` represents the memory in megabytes. With at least 10,000 connections available, even on the smallest servers. For example, on a server with 4GB memory (4,096 MB), the simultaneous connections are:

.. math::

    4\times 4096 = 16384 {\ connections}

.. note::
    
    Make sure to convert the memory figure ``m`` to megabytes.


This number is estimated by the exact available memory so it varies between different plans and cloud providers, to see the exact maximum connections allowed, use * :doc:`redis-cli <./connect-redis-cli>` and ``info`` command as the following:

.. code-block::

    echo "info" | redis-cli -u REDIS_URI | grep maxclients