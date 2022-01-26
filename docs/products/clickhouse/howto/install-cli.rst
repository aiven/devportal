Use the ClickHouse client
=========================

To use the ClickHouse client across different operating systems, we recommend utilizing `Docker <https://www.docker.com/>`_. You can get the latest image of the ClickHouse client directly from `the dedicated page in Docker hub <https://hub.docker.com/r/clickhouse/clickhouse-client>`_.

.. note::

    There are other installation options available for ClickHouse clients for certain operating systems. You can find them `in the official ClickHouse documentation <https://clickhouse.com/docs/en/getting-started/install/#available-installation-options>`_.

Connection properties
---------------------

You will need to know the following properties to establish a secure connection with your Aiven for ClickHouse service: **Host**, **Port**, **User** and **Password**. You will find these in the *Connection information* section in the *Overview* page of your service in the `Aiven web console <https://console.aiven.io/>`_.

Command template
-----------------

The command to connect to the service looks like this:

.. code:: bash

    docker run --interactive \
    --rm clickhouse/clickhouse-client \
    --user USER-NAME \
    --password USER-PASSWORD \
    --host YOUR-HOST-NAME.aivencloud.com \
    --port YOUR-PORT \
    --secure \
    --query="YOUR SQL QUERY GOES HERE"

This example includes the ``--interactive`` option (or ``-i``) to be able to access the command prompt outside the docker container and  the ``--rm`` option to automatically remove the container after exiting.

The other parameters, such as ``--user``, ``--password``, ``--host``, ``--port``, ``--secure``, and ``--query`` are arguments accepted by the ClickHouse client. You can see the full list of command line options in `the ClickHouse CLI documentation <https://clickhouse.com/docs/en/interfaces/cli/#command-line-options>`_.

Command example
-----------------

Here is an example of a request to see the list of present databases::

    docker run --interactive \
    --rm clickhouse/clickhouse-client \
    --user USER-NAME \
    --password USER-PASSWORD \
    --host YOUR-HOST-NAME.aivencloud.com \
    --port YOUR-PORT \
    --secure \
    --query="SHOW DATABASES"


