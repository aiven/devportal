Enable Apache Kafka® Connect connectors auto restart on failures
================================================================

If you experience an Apache Kafka® Connect connector failure, restarting automatically the task is generally not recommended. Perform a proper investigation on the problem's cause before attempting the restart to avoid experiencing similar problems in the future. However, sometimes a task can fail due to a rare problem like the dedicated node going out of memory due to a huge surge of data; in such cases, the automatic task restart usually solves the issue.

.. Note::

    We observed cases when the Debezium source connector for PostgreSQL® stopped working after the PostgreSQL maintenance update, due to PostgreSQL inability to create replication slots before failover. In such cases the connector automatic restart could be a valid solution to avoid the problem.

Enable connector automatic restart with Aiven console
-----------------------------------------------------

Aiven provides an option to enable automatic connector restart in case of edge situations. All our connectors support this option. For example, follow these steps to update of an existing Debezium-PostgreSQL connector:

1. In the `Aiven console <https://console.aiven.io/>`_, select the Aiven for Apache Kafka or Aiven for Apache Kafka Connect service pages where the connector is defined.

2. Select **Connectors**  from the left sidebar and select the connector to be updated.

3. Select the **Aiven** tab on the connectors page. 

5. Set the **Automatic restart** option to ``True``

Once you have enabled automatic restart, the connector will be restarted automatically whenever a failure is detected. 

.. Warning::

    Enabling this feature will restart the entire connector, not just the failed tasks.
