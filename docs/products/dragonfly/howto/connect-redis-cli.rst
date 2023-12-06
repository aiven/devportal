Connect with ``redis-cli``
===========================

This example demonstrates how to connect to Dragonfly using ``redis-cli``, which supports nearly all the same commands as it does for Redis®. For more information, see `Dragonfly CLI <https://www.dragonflydb.io/docs/development/cli>`_.

Variables
'''''''''

Replace the following placeholders in the code sample with the appropriate values:

==================      =============================================================
Variable                Description
==================      =============================================================
``DRAGONFLY_URI``       URL for the Dragonfly connection
==================      =============================================================

Pre-requisites
''''''''''''''

Ensure the following before proceeding:

1. The ``redis-cli`` client installed. This can be installed as part of the Redis server installation or as a standalone client. Refer to the `Redis Installation Guide <https://redis.io/docs/getting-started/tutorial/>`_ for more information.

Code
''''

To connect to Dragonfly, execute the following command in a terminal window:

.. code::

    redis-cli -u DRAGONFLY_URI

This command connects you to your Dragonfly instance.

To verify the connection is successful, use the ``INFO`` command:

.. code::

    INFO

This command should return various Dragonfly parameters similar to Redis:

.. code:: text

    # Server
    dragonfly_version:1.0.0
    dragonfly_git_sha1:0a1b2c3d
    dragonfly_mode:standalone
    ...

To set a key, use the following command:

.. code::

    SET mykey mykeyvalue123

This should return a confirmation ``OK``.

To retrieve the set key value, use:

.. code::

    GET mykey

The output will be the value of the key, in this case, ``"mykeyvalue123"``.
