Manage Apache Kafka® Connect logging level
==========================================

During the operation of an Aiven for Apache Kafka® Connect cluster, you may encounter errors from one or more running connectors. Sometimes the stack trace printed in the logs is useful in determining the root cause of an issue while other times, the information provided just isn't enough to work with.

Therefore you might need access to more detailed logs to debug an issue. This can be done for a specific logger or connector by setting the logging level of an Apache Kafka® Connect's cluster using the `Kafka Connect REST APIs <https://kafka.apache.org/documentation.html>`__.

.. Warning::

    The REST API only changes the logging level on the node that's accessed, not across an entire distributed Connect cluster. Therefore, for a multi-node cluster, you would have to change the logging level in all of the nodes that run the connector's tasks you wish to debug.

    For a dedicated Aiven for Apache Kafka® Connect cluster using a Startup plan, there is 1 node, while Business and Premium plan have 3 and 6 nodes respectively.

Modify the Kafka Connect logging level
--------------------------------------

The following procedure allows you to update the logging level in an Aiven for Apache Kafka Connect service.

Get the Kafka Connect nodes connection URI
''''''''''''''''''''''''''''''''''''''''''

To update the logging level in all the Kafka Connect nodes, you need to get their connection URI using the :ref:`Aiven CLI service get command <avn_service_get>`

::

    avn service get SERVICE_NAME  --format '{connection_info}'

.. Note::

    The above command will show the connection URI for each node in the form ``https://avnadmin:PASSWORD@IP_ADDRESS:PORT``

Retrieve the list of loggers and connectors
'''''''''''''''''''''''''''''''''''''''''''

You can retrieve the list of loggers, connectors and their current logging level on each worker using the dedicated ``/admin/loggers`` Kafka Connect API

::

    curl https://avnadmin:PASSWORD@IP_ADDRESS:PORT/admin/loggers --insecure

.. Tip::

    The ``--insecure`` parameter avoids ``curl`` non matching certificates error due to using the IP instead of the hostname

The output should be similar to the below

.. code-block:: json

    {
        "org.apache.zookeeper": {
            "level": "ERROR"
        },
        "org.reflections": {
            "level": "ERROR"
        },
        "root": {
            "level": "INFO"
        }
    }

.. Warning::

    If you have not previously set a logging level for a connector's logger class, then the list of loggers retrieved above will not show any logger level information of that connector's logger class, even if that connector is currently running in the Aiven for Apache Kafka Connect cluster. See the next section on how to change the logging level of a particular logger.

Change the logging level for a particular logger
''''''''''''''''''''''''''''''''''''''''''''''''

To change the logging level for a particular logger you can use the same ``admin/loggers`` endpoint appending the logger name (``LOGGER_NAME`` in the below command)

::

    curl -X PUT -H "Content-Type:application/json"          \
        -d '{"level": "TRACE"}'                             \
        https://192.168.0.1:443/admin/loggers/LOGGER_NAME   \
        --insecure

.. Warning::

    When the node is restarted, logging reverts back to using the logging properties defined in the ``log4j`` configuration file. In an Aiven for Apache Kafka® Connect cluster the default logging level is ``INFO``.

For example, when we set a custom log level for the logger ``io.debezium.connector.postgresql.connection`` to be ``TRACE``, then this is what you will see upon listing the logger levels:

.. code-block:: json

    "io.debezium.connector.postgresql.connection.AbstractMessageDecoder": {
        "level": "TRACE"
    },
    "io.debezium.connector.postgresql.connection.PostgresConnection": {
        "level": "TRACE"
    },
    "io.debezium.connector.postgresql.connection.PostgresDefaultValueConverter": {
        "level": "TRACE"
    },
    "io.debezium.connector.postgresql.connection.PostgresReplicationConnection": {
        "level": "TRACE"
    },
    "io.debezium.connector.postgresql.connection.pgproto.PgProtoMessageDecoder": {
        "level": "TRACE"
    }


A note about loggers
''''''''''''''''''''

Loggers are Java objects which trigger log events, and each log message produced by the application is sent to a specific logger. Loggers are arranged in hierarchies, for example the logger ``io.debezium.connector.postgresql.PostgresConnector`` is a child of the logger ``io.debezium.connector.postgresql``. When you define the logging level of a logger using the commands above, the logging level will be set for that logger and all of its children in the logger hierarchy.

By convention, loggers have the same name as the corresponding Java class.  Therefore, to get name of the logger of a particular connector, use the connector's classname. The classname is usually the first field of the connector config when you select a connector for creation in the Aiven Console. For example, the logger for the Debezium PostgreSQL® source connector is also its classname ``io.debezium.connector.postgresql``:

.. code-block:: json

    {
        "connector.class": "io.debezium.connector.postgresql"
    }
