Enable Apache Kafka Connect connectors auto restart on failures
===============================================================

If you experience an Apache Kafka Connect connector failure, restarting automatically the task is generally not recommended. Perform a proper investigation on the problem's cause before attempting the restart to avoid experiencing similar problems in the future. However, sometimes a task can fail due to a rare problem like the dedicated node going out of memory due to a huge surge of data; in such cases, the automatic task restart usually solves the issue. 

.. Note::

    We observed cases when the Debezium source connector for PostgreSQL stopped working after the PostgreSQL maintenance update, due to PostgreSQL inability to create replication slots before failover. In such cases the connector automatic restart could be a valid solution to avoid the problem.

Enable connector automatic restart with Aiven console
-----------------------------------------------------

Aiven provides an option to enable automatic connector restart in case of edge situations. All our connectors support this option. For example, follow these steps to update of an existing Debezium-PostgreSQL connector:

1. In the `Aiven console <https://console.aiven.io/>`_ navigate to the Aiven for Apache Kafka or Aiven for Apache Kafka Connect service pages where the connector is defined.

2. Select to the **Connectors** tab and click on the connector to be updated

3. Select the **Aiven** tab

4. set the **Automatic restart** option to ``True``

Once you enabled the automatic restart, the connector will be restarted every time a failure is detected by our management platform.

.. Warning::

    This feature restarts the whole connector, not only the failed tasks.
