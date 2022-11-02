Manage ClickHouse® dababases and tables
=======================================

Aiven supports a few tools enabling SQL commands. For managing your ClickHouse® databases and tables, you can choose between our query editor, the Play UI, and the ClickHouse® client.

Use the query editor
--------------------

Aiven for ClickHouse® includes a web-based query editor, which you can find on the *Query Editor* tab of your service in the  `Aiven web console <https://console.aiven.io/>`_.

The requests that you run through the query editor are executed on behalf of the default user and rely on the permissions granted to this user.

Examples of queries
^^^^^^^^^^^^^^^^^^^

Retrieve a list of current databases::

    SHOW DATABASES

Count rows::

    SELECT COUNT(*) FROM transactions.accounts

Create a new role::

    CREATE ROLE accountant

Alternatives
^^^^^^^^^^^^

The query editor is convenient if you want to run queries directly from the console on behalf of the default user. However, if you want to run requests using a different user, or if you expect a large size of the response, you can use :doc:`play <use-play>`, a built-in user interface accessible through HTTPS.

Use the play UI
---------------

ClickHouse® includes a built-in user interface for running SQL queries. You can access it from a web browser over the HTTPS protocol. Follow these steps to use it:

1. Log in to the `Aiven web console <https://console.aiven.io/>`_, choose the right project, and select your Aiven for ClickHouse service.
#. In the *Overview* tab, find *Connection information* and select **ClickHouse HTTPS**.
#. Copy the Service URI and navigate to ``SERVICE_URI/play`` from a web browser.
#. Set the *name* and the *password* of the user on whose behalf you want to run the queries.
#. Enter the body of the query.
#. Select **Run**.

.. note::
    The play interface is only available if you can connect directly to ClickHouse from your browser. If the service is :doc:`restricted by IP addresses </docs/platform/howto/restrict-access>` or in a :doc:`VPC without public access </docs/platform/howto/public-access-in-vpc>`, you can use the :doc:`query editor <use-query-editor>` instead.
    The query editor can be accessed directly from the console to run requests on behalf of the default user.

Use the ClickHouse® client
--------------------------

To use the ClickHous® client across different operating systems, we recommend utilizing `Docker <https://www.docker.com/>`_. You can get the latest image of the ClickHouse client directly from `the dedicated page in Docker hub <https://hub.docker.com/r/clickhouse/clickhouse-client>`_.

.. note::

    There are other installation options available for ClickHouse clients for certain operating systems. You can find them `in the official ClickHouse documentation <https://clickhouse.com/docs/en/integrations/sql-clients/clickhouse-client-local>`_.

Connection properties
^^^^^^^^^^^^^^^^^^^^^

You will need to know the following properties to establish a secure connection with your Aiven for ClickHouse service: **Host**, **Port**, **User** and **Password**. You will find these in the *Connection information* section in the *Overview* page of your service in the `Aiven web console <https://console.aiven.io/>`_.

Command template
^^^^^^^^^^^^^^^^

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
