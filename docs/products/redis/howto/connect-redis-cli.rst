Connect with ``redis-cli``
--------------------------

This example connects to a Redis™* service from ``redis-cli``.

Variables
'''''''''

These are the placeholders you will need to replace in the code sample:

==================      =============================================================
Variable                Description
==================      =============================================================
``REDIS_URI``           URL for Redis connection, from the service overview page
==================      =============================================================

Pre-requisites
''''''''''''''

For this example you will need:

1. The ``redis-cli`` client installed. You can install this as part of the `Redis server installation <https://redis.io/topics/quickstart>`_ or as standalone client.


Code
''''

Execute the following to from a terminal window:

::

    redis-cli -u REDIS_URI


This code connects to the Redis database.

To check the connection is working, execute the following code::

    INFO

The command returns all the Redis parameters:

.. code:: text

    # Server
    redis_version:6.2.3
    redis_git_sha1:c708fc4f
    redis_git_dirty:1
    redis_build_id:eca3e7fbe7ce45c7
    redis_mode:standalone
    ...

To set a key, execute the following command::

    SET mykey mykeyvalue123

The command should output a confirmation ``OK`` statement. 

To retrieve the key value, execute the following command::

    GET mykey

The result is the value of the key, in the above example ``"mykeyvalue123"``.
