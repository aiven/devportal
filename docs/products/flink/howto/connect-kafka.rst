Create an Apache Kafka®-based Apache Flink® table
==================================================

To build data pipelines, Apache Flink® requires you to map source and target data structures as `Flink tables <https://nightlies.apache.org/flink/flink-docs-stable/docs/dev/table/sql/create/#create-table>`_ within an application. You can accomplish this through the `Aiven Console <https://console.aiven.io/>`_ or :doc:`Aiven CLI </docs/tools/cli/service/flink>`. 

When creating an application to manage streaming data, you can create a Flink table that connects to an existing or new Aiven for Apache Kafka® topic to source or sink streaming data. To define a table over an Apache Kafka® topic, you need to specify the topic name, clearly define the columns' data format, and choose the appropriate connector type. Additionally, enter a clear and meaningful name to the table for reference when building data pipelines.

.. Warning::

    In order to define Flink's tables an :doc:`existing integration <create-integration>` needs to be available between the Aiven for Flink service and one or more Aiven for Apache Kafka services.

Create Apache Flink® table with Aiven Console
------------------------------------------------

To create a Apache Flink® table based on an Aiven for Apache Kafka® topic via the `Aiven Console <https://console.aiven.io/>`_:

1. In the Aiven for Apache Flink service page, select **Application** from the left sidebar.
2. Create a new application or select an existing one with Aiven for Apache Kafka integration. 

   .. note:: 
    
      If editing an existing application, create a new version to make changes to the source or sink tables.

3. In the **Create new version** screen, select **Add source tables**.
4. Select **Add new table** or select **Edit** if you want to edit an existing source table. 
5. In the **Add new source table** or **Edit source table** screen, select the Aiven for Apache Kafka service as the integrated service. 
6. In the **Table SQL** section, enter the SQL statement below to create the Apache Kafka-based Apache Flink:

   .. code::

        CREATE TABLE kafka (
        
        ) WITH (
            'connector' = 'kafka',
            'properties.bootstrap.servers' = '',
            'scan.startup.mode' = 'earliest-offset',
            'topic' = '',
            'value.format' = 'json',
            'value.format' = 'json'
        )
   
   The following are the parameters:

   * ``connector``: the **Kafka connector type**, between the **Apache Kafka SQL Connector** (value ``kafka``) for standard topic reads/writes and the **Upsert Kafka SQL Connector** (value ``upsert-kafka``) for changelog type of integration based on message key. 
   
     .. note::
            For more information on the connector types and the requirements for each, see the articles on :doc:`Kafka connector types </docs/products/flink/concepts/kafka-connectors>` and :doc:`the requirements for each connector type </docs/products/flink/concepts/kafka-connector-requirements>`.

   * ``properties.bootstrap.servers``: this parameter can be left empty since the connection details will be retrieved from the Aiven for Apache Kafka integration definition

   * ``topic``: the topic to be used as a source for the data pipeline. If you want to use a new topic that does not yet exist, write the topic name.

     .. Warning::
        By default, Flink will not be able to create Apache Kafka topics while pushing the first record automatically. To change this behavior, enable in the Aiven for Apache Kafka target service the ``kafka.auto_create_topics_enable`` option in **Advanced configuration** section.
    
   * ``key.format``: specifies the **Key Data Format**. If a value other than **Key not used** is selected, specify the fields from the SQL schema to be used as key. This setting is specifically needed to set message keys for topics acting as target of data pipelines.
   
   * ``value.format``: specifies the **Value Data Format**. Based on the message format in the Apache Kafka topic. 

     .. note:: 
        For Key and Value data format, the following options are available:  

        * ``json``: `JSON <https://nightlies.apache.org/flink/flink-docs-master/docs/connectors/table/formats/json/>`_
        * ``avro``: `Apache Avro <https://nightlies.apache.org/flink/flink-docs-master/docs/connectors/table/formats/avro/>`_
        * ``avro-confluent``: `Confluent Avro <https://nightlies.apache.org/flink/flink-docs-master/docs/connectors/table/formats/avro-confluent/>`_. For information, see :doc:`/docs/products/flink/howto/flink-confluent-avro`. 
7. To create a sink table, select **Add sink tables** and repeat steps 4-6 for sink tables.
8. In the **Create statement** section, create a statement that defines the fields retrieved from each message in a topic, additional transformations such as format casting or timestamp extraction, and :doc:`watermark settings </docs/products/flink/concepts/watermarks>`. 


Example: Define a Flink table using the standard connector over topic in JSON format   
------------------------------------------------------------------------------------

The Aiven for Apache Kafka service named ``demo-kafka`` contains a topic named  ``metric-topic`` holding a stream of service metrics in JSON format like:

.. code:: text

    {'hostname': 'sleepy', 'cpu': 'cpu3', 'usage': 93.30629927475789, 'occurred_at': 1637775077782}
    {'hostname': 'dopey', 'cpu': 'cpu4', 'usage': 88.39531418706092, 'occurred_at': 1637775078369}
    {'hostname': 'happy', 'cpu': 'cpu2', 'usage': 77.90860728236156, 'occurred_at': 1637775078964}
    {'hostname': 'dopey', 'cpu': 'cpu4', 'usage': 81.17372993952847, 'occurred_at': 1637775079054}

We can define a ``metrics_in`` Flink table by selecting ``demo-kafka`` as integration service and writing the following as SQL schema:

.. code:: sql 
    
    CREATE TABLE metrics_in (
        cpu VARCHAR,
        hostname VARCHAR,
        usage DOUBLE,
        occurred_at BIGINT,
        time_ltz AS TO_TIMESTAMP_LTZ(occurred_at, 3),
        WATERMARK FOR time_ltz AS time_ltz - INTERVAL '10' SECOND
        )
    WITH (
        'connector' = 'kafka',
        'properties.bootstrap.servers' = '',
        'topic' = 'metric-topic',
        'value.format' = 'json',
        'scan.startup.mode' = 'earliest-offset'
        )  


.. Note::

    The SQL schema includes:

    * the message fields ``cpu``, ``hostname``, ``usage``, ``occurred_at`` and the related `data type <https://nightlies.apache.org/flink/flink-docs-release-1.16/docs/dev/table/types/#list-of-data-types>`_. The order of fields in the SQL definition doesn't need to follow the order presented in the payload.
    * the definition of the field ``time_ltz`` as transformation to ``TIMESTAMP(3)`` from the ``occurred_at`` timestamp in Linux format.
    * the ``WATERMARK`` definition

Example: Define a Flink table using the standard connector over topic in Avro format   
------------------------------------------------------------------------------------

In cases when target of the Flink data pipeline needs to write in Avro format to a topic named  ``metric_topic_tgt`` within the Aiven for Apache Kafka service named ``demo-kafka``.

You can define a ``metric_topic_tgt`` Flink table by selecting the ``demo-kafka`` as integration service and writing the following SQL schema:

.. code:: sql 

    CREATE TABLE metric_topic_tgt (
        cpu VARCHAR,
        hostname VARCHAR,
        usage DOUBLE
        )
    WITH (
        'connector' = 'kafka',
        'properties.bootstrap.servers' = '',
        'topic' = 'metric-topic',
        'value.format' = 'avro',
        'scan.startup.mode' = 'earliest-offset'
        ) 

.. Note::

    The SQL schema includes the output message fields ``cpu``, ``hostname``, ``usage`` and the related `data type <https://nightlies.apache.org/flink/flink-docs-release-1.16/docs/dev/table/types/#list-of-data-types>`_.


Example: Define a Flink table using the upsert connector over topic in JSON format   
------------------------------------------------------------------------------------

In cases when target of the Flink pipeline needs to write in JSON format and upsert mode to a compacted topic named  ``metric_topic_tgt`` within the Aiven for Apache Kafka service named ``demo-kafka``.

You can define a ``metric_topic_tgt`` Flink table by selecting ``demo-kafka`` as integration service and writing the following SQL schema:

.. code:: sql 

    CREATE TABLE metric_topic_tgt (
        cpu VARCHAR,
        hostname VARCHAR,
        max_usage DOUBLE,
        PRIMARY KEY (cpu, hostname) NOT ENFORCED
        )
    WITH (
        'connector' = 'upsert-kafka',
        'properties.bootstrap.servers' = '',
        'topic' = 'metric-topic',
        'value.format' = 'json',
        'scan.startup.mode' = 'earliest-offset'
        ) 

.. Note::

    Unlikely the standard Apache Kafka SQL connector, when using the Upsert Kafka SQL connector the key fields are not defined. They are derived by the ``PRIMARY KEY``  definition in the SQL schema.

.. Note::

    The SQL schema includes:
    
    * the output message fields ``cpu``, ``hostname``, ``max_usage`` and the related `data type <https://nightlies.apache.org/flink/flink-docs-release-1.16/docs/dev/table/types/#list-of-data-types>`_.
    * the ``PRIMARY KEY`` definition, driving the key part of the Apache Kafka message

