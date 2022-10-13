Handle PostgreSQL® node replacements when using Debezium for change data capture
=================================================================================

When running a :doc:`Debezium source connector for PostgreSQL® <debezium-source-connector-pg>` to capture changes from an Aiven for PostgreSQL® service, there are some activities on the database side that could impact the correct functionality of the connector.

As example, when the source PostgreSQL service undergoes any operation which replaces the nodes (such as maintenance, a plan or cloud region change or a node replacement), the Debezium connector loses connection to the PostgreSQL database. 
The connector is able to recover from temporary errors to the database and start listening for change events again after a restart of the related task. However, in some cases, the PostgreSQL replication slot used by Debezium can start lagging and therefore cause a growing amount of WAL logs.

.. Tip::
   
   There is a GitHub repository where you can easily spin up a Debezium - PostgreSQL setup to test the node replacement scenario and also follow along this `Aiven Debezium help article <https://github.com/aiven/debezium-pg-kafka-connect-test>`__.


Common Debezium errors related to PostgreSQL node replacement
-------------------------------------------------------------

In cases when the Debezium connector can't recover during or after the PostgreSQL node replacements, the following errors are commonly shown in logs::

   # ERROR 1
   org.apache.kafka.connect.errors.ConnectException: Could not create PostgreSQL connection
   # ERROR 2
   io.debezium.DebeziumException: Could not execute heartbeat action (Error: 57P01)
   # ERROR 3
   org.PostgreSQL.util.PSQLException: ERROR: replication slot "SLOT_NAME" is active for PID xxxx

The above errors are unrecoverable, meaning that they require a restart of the connector task(s) in order to resume operations again. 

A restart can be performed manually either through the `Aiven Console <https://console.aiven.io/>`_, in under the `Connectors` tab console or via the `Apache Kafka® Connect REST API <https://docs.confluent.io/platform/current/connect/references/restapi.html#rest-api-task-restart>`__. You can get the service URI from the `Aiven Console <https://console.aiven.io/>`_, in the service detail page.

.. image:: /images/products/postgresql/pg-debezium-cdc_image.png
   :alt: The Aiven Console page showing the Debezium connector error

.. Tip::

   For automatically restarting tasks, you can set ``"_aiven.restart.on.failure": true`` in the connector's configuration ( `check the related article <https://help.aiven.io/en/articles/5088396-kafka-connect-auto-restart-on-failures>`__). Aiven automatically check tasks status for errors every 15 minutes but the interval can be customised if needed.



Handle growing replication lag after Debezium connector restart
---------------------------------------------------------------

As per the `dedicated Debezium docs <https://debezium.io/documentation/reference/stable/connectors/postgresql.html#postgresql-wal-disk-space>`_, there are two main reasons why growing replication lag can happen after the Debezium connector is restarted:

#. Too many updates are happening in the tracked database but only a tiny number of updates are related to the table(s) and schema(s) for which the connector is capturing changes. 

   Such issue can be resolved by enabling periodic heartbeat events and setting the (``heartbeat.interval.ms``) connector configuration property.

#. The PostgreSQL instance contains multiple databases and one of them is a high-traffic database. 

   Debezium captures changes in another database that is low-traffic in comparison to the other database. Debezium then cannot confirm the LSN (``confirmed_flush_lsn``) as replication slots work per-database and Debezium is not invoked. As WAL is shared by all databases, the amount used tends to grow until an event is emitted by the database for which Debezium is capturing changes.

During the Aiven testing, the above situations have been observed to happen in 2 scenarios:

#. The table(s) which the Debezium connector is tracking has not had any changes, and heartbeats are not enabled in the connector.

#. The table(s) which the Debezium connector is tracking has not had any changes, heartbeats are enabled (via ``heartbeat.interval.ms`` and ``heartbeat.action.query``), but the connector is not sending the heartbeat. 

   .. Note::
   
      The Debezium heartbeat problem is discussed in the bug `DBZ-3746 <https://issues.redhat.com/browse/DBZ-3746>`__ .

Clear the replication lag
~~~~~~~~~~~~~~~~~~~~~~~~~

To clear the replication lag, resume the database activities (if have paused all traffic to the database) or make any changes to the tracked tables to invoke the replication slot. Debezium would then confirm the latest LSN and allow the database to reclaim the WAL space.

Ensure Debezium gracefully survives a PostgreSQL node replacement
-----------------------------------------------------------------

To prevent data loss (Debezium missing change events) during PostgreSQL node replacement and ensure the automatic recovery of the connector, follow the guidelines below.

React to Debezium failures
~~~~~~~~~~~~~~~~~~~~~~~~~~

The following guideline ensures no data loss in case of a Debezium connector failure and requires disabling writes to the source PoistgreSQL database.

1. After noticing a failed Debezium connector, stop all the write traffic to the database immediately.
   
   After a node replacement, replication slots are not recreated automatically in the newly promoted database. When Debezium recovers, it will recreate the replication slot.If there were changes made to the database before the replication slot is recreated on the new primary server, then Debezium will not be able to capture them, resulting in data loss. 

   When this happens, you can reconfigure the connector to temporarily use ``snapshot.mode=always``, then restart the connector. This settings forces the connector to republish snapshot data again to the output Apache Kafka® topics. Reconfigure it back to the default once the snapshot finishes to avoid regenerating snapshot on every restart.

2. Manually restart the failed task(s)

3. Confirm that the connector has created a new replication slot and that it is in active state by querying the ``pg_replication_slots`` table

4. Resume the write operations on the database.

Automate the replication slot re-creation and verification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following guideline requires the setup of an automation which re-creates the replication slot on the new PostgreSQL nodes. As per `Debezium docs <https://debezium.io/documentation/reference/stable/connectors/postgresql.html#postgresql-cluster-failures>`_:

   There must be a process that re-creates the Debezium replication slot before allowing applications to write to the new primary. This is crucial. Without this process, your application can miss change events.

After recovering, the Debezium connector can create the replication slot on the newly promoted database if none exists, however there can be some delay in doing that. Having a separate and automated process recreating the Debezium replication slot immediately after a node replacement is fundamental to resume normal operations as soon as possible without data loss. When the connector recovers, it will capture all the changes that are made *after* the replication slot was created.

.. Tip:

   The example contained in the `dedicated Aiven repository <https://github.com/aiven/debezium-pg-kafka-connect-test/blob/6f1e6e829ba06bbc396fc0faf28be9e0268ad4f8/bin/python_scripts/debezium_pg_producer.py#L164>`__ demonstrates a basic functionality of disabling inserts to the database unless the Debezium replication slot is active. However, it is enough to check that the replication slot to exists although it may be inactive - meaning the connector isn't actively listening on the slot yet. Once the connector starts listening again, it will capture all the change events since the replication slot was created.

The `Debezium docs <https://debezium.io/documentation/reference/stable/connectors/postgresql.html#postgresql-cluster-failures>`__ also suggest:

   Verify that Debezium was able to read all changes in the slot before the old primary failed.

To ensure that client applications that depend on events captured by Debezium get all the events, you need to implement a method to verify that all changes made to the tables that Debezium is capturing from are recorded. 

.. Tip::

   The example contained in the `dedicated Aiven repository <https://github.com/aiven/debezium-pg-kafka-connect-test/blob/53da8ee8fde8bf7802fd5bbb6aa39359cd1c0877/bin/python_scripts/debezium_pg_producer.py#L66>`__ demonstrates this implementation.

As per above guideline, setting ``"_aiven.restart.on.failure": true`` on all Debezium connectors ensures that failed tasks are automatically restarted in case they fail. By default tasks status is checked every 15 minutes but the interval can be customised if needed.