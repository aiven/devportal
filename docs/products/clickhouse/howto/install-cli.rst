Use ClickHouse client
=======================

To be able to use ClickHouse client across different operating systems, we recommend utilizing `Docker <https://www.docker.com/>`_. The latest image of ClickHouse client can be pulled directly from `the dedicated page in Docker hub <https://hub.docker.com/r/clickhouse/clickhouse-client>`_.

.. note::

    There are other installation options available for ClickHouse client specific for certain operating systems. You can find them `in the official documentation of ClickHouse <https://clickhouse.com/docs/en/getting-started/install/#available-installation-options>`_.

Connection properties
---------------------

You will need to know the following properties to establish a secure connection with the ClickHouse server: **Host**, **Port**, **User** and **Password**. They can be found in the *Connection information* section in the *Overview* page of your service in `Aiven web console <https://console.aiven.io/>`_.

Command template
-----------------

The generic command to connect to the server will look like this:

.. code:: bash

    docker run --interactive \
    --rm clickhouse/clickhouse-client \
    --user USER-NAME \
    --password USER-PASSWORD \
    --host YOUR-HOST-NAME.aivencloud.com \
    --port YOUR-PORT \
    --secure \
    --query="YOUR SQL QUERY GOES HERE"

We include options ``--interactive`` (or ``-i``) to be able to access the command prompt outside of docker container and  ``--rm`` to automatically remove the container after exiting.

The rest of parameters, such as ``--user``, ``--password``, ``host``, ``port``, ``secure`` and ``query`` are arguments accepted by ClickHouse client. The full list of command line options can be found in `the ClickHouse CLI documentation <https://clickhouse.com/docs/en/interfaces/cli/#command-line-options>`_.

Command example
-----------------

Below is an example of a request to create a new database::

    docker run --interactive \
    --rm clickhouse/clickhouse-client \
    --user USER-NAME \
    --password USER-PASSWORD \
    --host YOUR-HOST-NAME.aivencloud.com \
    --port YOUR-PORT \
    --secure \
    --query="CREATE DATABASE IF NOT EXISTS a-new-and-shiny-database"


