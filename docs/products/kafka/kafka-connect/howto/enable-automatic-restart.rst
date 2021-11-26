Enable Apache Kafka Connect connectors auto restart on failures
===============================================================

In case of an Apache Kafka Connect connector failure, automatic task restart is generally not recommended. Proper investigation on the problem's cause should be performed before attempting to restart the failed connector to avoid experiencing similar problems in the future. However, sometimes a task can fail due to a rare problem like the dedicated node going out of memory due to a huge surge of data. 

.. Note::

    We observed cases when, using the Debezium source connector for PostgreSQL, the Apache Kafka connector stopped working after the PostgreSQL maintenance update, due to the PostgreSQL inability to create replication slots before failover. In such cases the connector automatic restart could be a valid solution to avoid the problem.

Enable connector automatic restart with Aiven console
-----------------------------------------------------

Aiven provides an option, applicable to all connectors, to enable automatic connector restart in case of edge situations. The following takes the update of an existing Debezium-PostgreSQL connector as an example:

1. In the `Aiven console <https://console.aiven.io/>`_ navigate to the Aiven for Apache Kafka or Aiven for Apache Kafka Connect service pages where the connector is defined.

2. Select to the **Connectors** tab and click on the connector to be updated

3. Select the **Aiven** tab

4. set the **Automatic restart** option to ``True``

.. image:: /images/products/kafka/kafka-connect/set-automatic-restart-true.png
   :alt: Aiven console with Automatic restart option set to True

After enabling the automatic restart, when failures have been detected by our management platform, the connector is restarted.

.. Warning::

    This feature restarts the whole connector, not only the failed tasks.
