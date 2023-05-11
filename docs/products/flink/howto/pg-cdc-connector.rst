Create a PostgreSQL® CDC connector-based Apache Flink®
===========================================================

Change Data Capture (CDC) is a technique that enables the tracking and capturing of changes made to data within a PostgreSQL® database. By identifying and capturing changes at the granular row level, CDC enables applications to react and promptly process these changes in real time. This ensures up-to-date data accuracy and minimizes the latency involved in processing updates.

When using Aiven for Apache Flink®, you can seamlessly leverage the power of the PostgreSQL CDC Connector to stream and process real-time data changes from PostgreSQL databases. Integrated with the Debezium engine, the CDC connector captures changes at the granular level of each table within an event stream. 

This article provides you with information on how to create a PostgreSQL CDC connector-based Apache Flink® table. 

Prerequisites
--------------
Before setting up the PostgreSQL CDC Connector with Aiven for Apache Flink, ensure that you have the following prerequisites in place:

* Running Aiven for Apache Flink® Service
* Running Aiven for Apache Kafka® Service
* Running Aiven for PostgreSQL® Service
* Integration between Aiven for Flink and Aiven for PostgreSQL: Establish the necessary integration between your Aiven for Apache Flink service and Aiven for PostgreSQL service. 

In addition to the above, gather the following information about the source PostgreSQL database:

* ``Hostname``: The hostname or IP address of the PostgreSQL server where your source database is located.
* ``Port``: The port number on which the PostgreSQL server is listening for incoming connections.
* ``Database name``: The name of the source database within the PostgreSQL server.
* ``Username``: The username used to authenticate and access the PostgreSQL database.
* ``Password``: The password associated with the provided username for authentication.
* ``Schema name``: The schema name where the source table is located within the database.
* ``Table name``: The name of the source table from which you want to capture data changes.
* ``Decoding plugin name``: The decoding plugin name to use for capturing the changes. For PostgreSQL CDC, set it as ``pgoutput``.

.. important:: 
    To create a PostgreSQL CDC source connector in Aiven for Apache Flink with Aiven for PostgreSQL using the pgoutput plugin, you need to have superuser privileges.


Configure the PostgreSQL CDC connector 
---------------------------------------
Follow these steps to configure the PostgreSQL CDC Connector in the Aiven for Flink application table using the `Aiven Console <https://console.aiven.io/>`_:

1. In the Aiven for Apache Flink service page, open the **Application** tab.
2. Select **Create new application**, enter the name of your application, and select **Create application**. 

.. note::    
    If editing an existing application, create a new version to make changes to the source or sink tables.

3. Select **Create first version** to create the first version of the application.
4. Select **Add your first source table** to add a source table.
5. In the **Add new source table** screen, select the *Aiven for PostgreSQL®* service as the integrated service.
6. In the **Table SQL** section, enter the SQL statement to create the PostgreSQL-based Apache Flink table with CDC connector. For example: 

.. code:: 

    CREATE TABLE test_table (
        column1 INT,
        column2 VARCHAR
        ) WITH (
        'connector' = 'postgres-cdc',
        'hostname' = 'test-project-test.avns.net',
        'username' = 'username',
        'password' = '12345',
        'schema-name' = 'public',
        'table-name' = 'test-1',
        'port' = '12709',
        'database-name' = 'defaultdb',
        'decoding.plugin.name' = 'pgoutput'
        )

Where: 

* ``connector``: The connector type to be used, which is ``postgres-cdc`` in this case.
* ``hostname``: The hostname or address of the PostgreSQL database server. 
* ``username``: The username to authenticate with the PostgreSQL database.
* ``password``: The password for the provided username.
* ``schema-name``: The name of the schema where the source table is located, which is set to ``public`` in the example.
* ``table-name``: The name of the source table to be captured by the CDC connector, which is set to ``test-1`` in the example.
* ``port``: The port number of the PostgreSQL database server.
* ``database-name``: The name of the database where the source table resides, which is set to ``defaultdb`` in the example.
* ``decoding.plugin.name``: The decoding plugin to be used by the CDC connector, which is set to ``pgoutput`` in the example.

8. Select **Next** to add the sink table, and then select **Add your first sink table**. Select *Aiven for Apache Kafka®* as the integrated service from the drop-down list.
9.  In the **Table SQL** section, input the SQL statement for creating the sink table where the PostgreSQL CDC connector will send the data. ßßSelect **Add table**.
10. In the **Create statement** section, write the SQL schema that defines the fields retrieved from the PostgreSQL® table and any additional transformations.



