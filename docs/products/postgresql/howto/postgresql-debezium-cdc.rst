Handle PostgreSQL® node replacements when using Debezium for change data capture
=================================================================================

As an Aiven customer you may be running a Aiven for Apache Kafka® Connect cluster that runs one or more `Debezium PostgreSQL® source connectors <https://docs.aiven.io/docs/products/kafka/kafka-connect/howto/debezium-source-connector-pg.html>`__ (Debezium) capturing changes from an Aiven for PostgreSQL® service.

After the PostgreSQL service has had a maintenance update or undergo any operation which replaces the nodes (such as a plan or cloud region change), Debezium would lose connection to the PostgreSQL database. It is able to recover from connection errors to the database and start listening for change events again after a restart of the connector's task. However, in some cases the Debezium replication slot is lagging behind as the amount of WAL logs grows causing a concern.

.. Tip::
   
   There is a GitHub repository where you can easily spin up a Debezium - PostgreSQL setup to test the node replacement scenario and also follow along this `Aiven Debezium help article <https://github.com/aiven/debezium-pg-kafka-connect-test>`__.

The possible errors encountered, the cause and solution to the growing replication slot lag, and how to ensure a graceful PostgreSQL node replacement or maintenance upgrade are explained in the next sections.


Debezium errors related to PostgreSQL node replacement
------------------------------------------------------------------------------

During the reported PostgreSQL node replacements where Debezium could not recover, we have observed the following errors that have occurred in one or more occasions::

   # ERROR 1
   org.apache.kafka.connect.errors.ConnectException: Could not create PostgreSQL connection
   # ERROR 2
   io.debezium.DebeziumException: Could not execute heartbeat action (Error: 57P01)
   # ERROR 3
   org.PostgreSQL.util.PSQLException: ERROR: replication slot "SLOT_NAME" is active for PID xxxx

These are all unrecoverable errors, meaning that they require a restart of the connector task(s) in order to resume operations again. A restart can be performed manually either through the `Aiven Console <https://console.aiven.io/>`_, in under the `Connectors` tab console or via the `Kafka Connect REST API <https://docs.confluent.io/platform/current/connect/references/restapi.html#rest-api-task-restart>`__. You can get the service URI from the `Aiven Console <https://console.aiven.io/>`_, in the service detail page.

.. image:: /images/products/postgresql/pg-debezium-cdc_image1.png

.. Tip::

   For automatically restarting tasks due to unrecoverable errors, we can set ``"_aiven.restart.on.failure": true`` in the connector's configuration ( `help article <https://help.aiven.io/en/articles/5088396-kafka-connect-auto-restart-on-failures>`__). By default tasks are checked for errors every 15 minutes but we can set this to something else. Please contact Aiven support if you would like to have this check interval shortened.



Growing replication lag after Debezium connector restart
-----------------------------------------------------------------------------------

Per the Debezium docs, there are two reasons why growing replication lag can happen after Debezium connector restart:

#. Too many updates in the tracked database but only a tiny number of updates are related to the table(s) and schema(s) for which the connector is capturing changes. Such issue can be resolved with periodic heartbeat events and set the (``heartbeat.interval.ms``) connector configuration property.

#. The PostgreSQL instance contains multiple databases and one of them is a high-traffic database. Debezium captures changes in another database that is low-traffic in comparison to the other database. Debezium then cannot confirm the LSN (``confirmed_flush_lsn``) as replication slots work per-database and Debezium is not invoked. As WAL is shared by all databases, the amount used tends to grow until an event is emitted by the database for which Debezium is capturing changes.

During testing, this has been observed to happen in 2 scenarios:

#. The table(s) which the Debezium connector is tracking has not had any
   changes, and heartbeats are not enabled in the connector.

#. The table(s) which the Debezium connector is tracking has not had any changes, heartbeats are enabled (via ``heartbeat.interval.ms`` and ``heartbeat.action.query``), but the connector is not sending the heartbeat. 

   Debezium not sending the heartbeat is a known bug reported in `DBZ-3746 <https://issues.redhat.com/browse/DBZ-3746>`__ .

Clear the replication lag
~~~~~~~~~~~~~~~~~~~~~~~~~

To clear the lag, simply resume the database activities (assuming you have paused all traffic to the database) or make some changes to any table in the database in which Debezium is capturing changes to invoke the replication slot (such as the heartbeat table). Debezium would then confirm the latest LSN and allow the database to reclaim the WAL space.

Ensure Debezium gracefully survives a PostgreSQL node replacement
-----------------------------------------------------------------

To prevent data loss (Debezium missing change events) in the event of a PostgreSQL node replacement and ensure the automatic recovery of the connector, here are several guidelines which you can follow.

Immediate solutions
~~~~~~~~~~~~~~~~~~~

1. Stop all changes to the database immediately after noticing that Debezium connector has failed.
   
   After a node replacement, replication slots are not recreated automatically in the newly promoted database. When Debezium recovers, it will recreate the replication slot.
   
   If there were changes made to the database before the replication slot is recreated on the new primary server, then Debezium will not be able to capture them, resulting in data loss. When this happens, you can reconfigure the connector to temporarily use ``snapshot.mode=always``, then restart the connector. This forces the connector to republish snapshot data again to the output Kafka topics. Remember to reconfigure it back after the snapshot finishes to avoid having a snapshot regenerated again on the next restart.

2. Manually restart the failed task(s) either through the web console or via the `Kafka Connect REST API <https://docs.confluent.io/platform/current/connect/references/restapi.html#rest-api-task-restart>`_ (can get URL from web console), and then once confirming that the connector has created a new replication slot and that it is in active state (query from ``pg_replication_slots`` view), we can resume normal operations on the database.

Long-term solutions
~~~~~~~~~~~~~~~~~~~

The `Debezium docs <https://debezium.io/documentation/reference/1.5/connectors/postgresql.html#postgresql-cluster-failures>`_ suggest the following:

   There must be a process that re-creates the Debezium replication slot before allowing applications to write to the new primary. This is crucial. Without this process, your application can miss change events.

Once recovered, the Debezium connector can also create the replication slot on the newly promoted database if none exists, however there can be some delay for whatever reasons until the connector recovers, so having a separate process recreate the Debezium replication slot immediately after a node replacement is important if we want to resume normal operations as soon as possible. When the connector recovers, it will capture all the changes that are made *after* the replication slot was created.

`This example
script <https://github.com/aiven/debezium-pg-kafka-connect-test/blob/6f1e6e829ba06bbc396fc0faf28be9e0268ad4f8/bin/python_scripts/debezium_pg_producer.py#L164>`__ demonstrates a basic functionality of not allowing inserts to the database unless the Debezium replication slot is active. However, it is enough to check that the replication slot to exists although it may be inactive - meaning the connector isn't actively listening on the slot yet. Once the connector starts listening again, it will capture all the change events since the replication slot was created.

   Verify that Debezium was able to read all changes in the slot before the old primary failed.

To ensure that client applications that depend on events captured by Debezium get all the events, implement a way to verify that all changes made to the tables that Debezium is capturing from are recorded. The same `example script mentioned above <https://github.com/aiven/debezium-pg-kafka-connect-test/blob/53da8ee8fde8bf7802fd5bbb6aa39359cd1c0877/bin/python_scripts/debezium_pg_producer.py#L66>`__ demonstrates this implementation.

   Set ``"_aiven.restart.on.failure": true`` on all Debezium connectors to ensure that failed tasks are automatically restarted in case they fail. By default this is checked every 15 minutes but we can set this to happen more frequently.