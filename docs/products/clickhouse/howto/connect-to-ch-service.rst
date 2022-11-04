Connect to a ClickHouse® cluster
================================

It's recommended to connect to a ClickHouse® cluster with the ClickHouse® client.

Use the ClickHouse® client
--------------------------

To use the ClickHouse® client across different operating systems, we recommend utilizing `Docker <https://www.docker.com/>`_. You can get the latest image of the ClickHouse client directly from `the dedicated page in Docker hub <https://hub.docker.com/r/clickhouse/clickhouse-client>`_.

.. note::

    There are other installation options available for ClickHouse clients for certain operating systems. You can find them `in the official ClickHouse documentation <https://clickhouse.com/docs/en/install/#available-installation-options>`_.

Connection properties
---------------------

You will need to know the following properties to establish a secure connection with your Aiven for ClickHouse service: **Host**, **Port**, **User** and **Password**. You will find these in the *Connection information* section in the *Overview* page of your service in the `Aiven web console <https://console.aiven.io/>`_.

Command template
----------------

The command to connect to the service looks like this, substitute the placeholders for ``USERNAME``, ``PASSWORD``, ``HOST`` and ``PORT``:

.. code:: bash

    docker run -it \
    --rm clickhouse/clickhouse-client \
    --user USERNAME \
    --password PASSWORD \
    --host HOST \
    --port PORT \
    --secure

This example includes the ``-it`` option (a combination of ``--interactive`` and ``--tty``) to take you inside the container and  the ``--rm`` option to automatically remove the container after exiting.

The other parameters, such as ``--user``, ``--password``, ``--host``, ``--port``, ``--secure``, and ``--query`` are arguments accepted by the ClickHouse client. You can see the full list of command line options in `the ClickHouse CLI documentation <https://clickhouse.com/docs/en/interfaces/cli/#command-line-options>`_.

Once you're connected to the server, you can type queries directly within the client, for example, to see the list of existing databases, run

.. code:: sql

    SHOW DATABASES


Alternatively, sometimes you might want to run individual queries and be able to access the command prompt outside the docker container. In this case you can set ``--interactive`` and  use ``--query`` parameter without entering the docker container:

.. code:: bash

    docker run --interactive            \
    --rm clickhouse/clickhouse-client   \
    --user USERNAME                     \
    --password PASSWORD                 \
    --host HOST                         \
    --port PORT                         \
    --secure                            \
    --query="YOUR SQL QUERY GOES HERE"

Similar to above example, you can request the list of present databases directly::

    docker run --interactive            \
    --rm clickhouse/clickhouse-client   \
    --user USERNAME                     \
    --password PASSWORD                 \
    --host HOST                         \
    --port PORT                         \
    --secure                            \
    --query="SHOW DATABASES"
