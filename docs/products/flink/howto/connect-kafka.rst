Create an Apache Kafka®-based Apache Flink® table
==================================================

To build data pipelines, Apache Flink® requires you to map source and target data structures as `Flink tables <https://nightlies.apache.org/flink/flink-docs-stable/docs/dev/table/sql/create/#create-table>`_ within an application. You can accomplish this through the `Aiven Console <https://console.aiven.io/>`_ or :doc:`Aiven CLI </docs/tools/cli/service/flink>`. 

When creating an application to manage streaming data, you can create a Flink table that connects to an existing or new Aiven for Apache Kafka® topic to source or sink streaming data. To define a table over an Apache Kafka® topic, you need to specify the topic name, clearly define the columns' data format, and choose the appropriate connector type. Additionally, enter a clear and meaningful name to the table for reference when building data pipelines.

.. Warning::

    In order to define Flink's tables an :doc:`existing integration <create-integration>` needs to be available between the Aiven for Flink service and one or more Aiven for Apache Kafka services.

Create Apache Flink® table with Aiven Console
------------------------------------------------

To create a Apache Flink® table based on an Aiven for Apache Kafka® topic via the `Aiven Console <https://console.aiven.io/>`_:

1. In the Aiven for Apache Flink service page, open the **Application** tab.
2. :doc:`Create a new application <../howto/create-flink-applications>` or select an existing one with Aiven for Apache Kafka integration. 

.. note:: 
    If editing an existing application, create a new version to make changes to the source or sink tables.

3. In the **Create new version** screen, click **Add source tables**.
4. Click **Add new table** or click **Edit** if you want to edit an existing source table. 
5. In the **Add new source table** or **Edit source table** screen, select the Aiven for Apache Kafka service as the integrated service. 
6. In the **Table SQL** section, enter the SQL statement to create the Apache Kafka-based Apache Flink table with the following details: 

   * The topic to be used as a source for the data pipeline. If you want to use a new topic that does not yet exist, write the topic name.

    .. Warning::
        By default, Flink will not be able to create Apache Kafka topics while pushing the first record automatically. To change this behavior, enable in the Aiven for Apache Kafka target service the ``kafka.auto_create_topics_enable`` option in **Advanced configuration** section.

   * Specify the **Kafka connector type**, between the **Apache Kafka SQL Connector** for standard topic reads/writes and the **Upsert Kafka SQL Connector** for changelog type of integration based on message key. 
   
    .. note::
        For more information on the connector types and the requirements for each, see the articles on :doc:`Kafka connector types </docs/products/flink/concepts/kafka-connectors>` and :doc:`the requirements for each connector type </docs/products/flink/concepts/kafka-connector-requirements>`.
    
   * Specify the **Key Data Format**. If a value other than **Key not used** is selected, specify the fields from the SQL schema to be used as key. This setting is specifically needed to set message keys for topics acting as target of data pipelines.
   * Specify the **Value Data Format**. Based on the message format in the Apache Kafka topic. 

    .. note:: 
        For Key and Value data format, the following options are available:  

        * `JSON <https://nightlies.apache.org/flink/flink-docs-master/docs/connectors/table/formats/json/>`_
        * `Apache Avro <https://nightlies.apache.org/flink/flink-docs-master/docs/connectors/table/formats/avro/>`_
        * `Confluent Avro <https://nightlies.apache.org/flink/flink-docs-master/docs/connectors/table/formats/avro-confluent/>`_
        * `Debezium Avro <https://nightlies.apache.org/flink/flink-docs-master/docs/connectors/table/formats/debezium/>`_
        * `Debezium JSON <https://nightlies.apache.org/flink/flink-docs-master/docs/connectors/table/formats/debezium/>`_
7. To create a sink table, click **Add sink tables** and repeat steps 4-6 for sink tables.
8. Create a statement that defines the fields retrieved from each message in a topic, additional transformations such as format casting or timestamp extraction, and :doc:`watermark settings <../concepts/watermarks>`. 


Example: Define a Flink table using the standard connector over topic in JSON format   
------------------------------------------------------------------------------------

The Aiven for Apache Kafka service named ``demo-kafka`` contains a topic named  ``metric-topic`` holding a stream of service metrics in JSON format like:

.. code:: text

    {'hostname': 'sleepy', 'cpu': 'cpu3', 'usage': 93.30629927475789, 'occurred_at': 1637775077782}
    {'hostname': 'dopey', 'cpu': 'cpu4', 'usage': 88.39531418706092, 'occurred_at': 1637775078369}
    {'hostname': 'happy', 'cpu': 'cpu2', 'usage': 77.90860728236156, 'occurred_at': 1637775078964}
    {'hostname': 'dopey', 'cpu': 'cpu4', 'usage': 81.17372993952847, 'occurred_at': 1637775079054}

We can define a ``metrics_in`` Flink table with:

* ``demo-kafka`` as integration service
* ``metric-topic`` as Apache Kafka topic name
* **Apache Kafka SQL Connector** since we want to threat every entry as unique events
* **Key not used** as Key data format
* **JSON** as Value data format
* ``metrics_in`` as Flink table name
* The following as SQL schema

.. code:: sql 

    cpu VARCHAR,
    hostname VARCHAR,
    usage DOUBLE,
    occurred_at BIGINT,
    time_ltz AS TO_TIMESTAMP_LTZ(occurred_at, 3),
    WATERMARK FOR time_ltz AS time_ltz - INTERVAL '10' SECOND

.. Note::

    The SQL schema includes:

    * the message fields ``cpu``, ``hostname``, ``usage``, ``occurred_at`` and the related `data type <https://nightlies.apache.org/flink/flink-docs-release-1.15/docs/dev/table/types/#list-of-data-types>`_. The order of fields in the SQL definition doesn't need to follow the order presented in the payload.
    * the definition of the field ``time_ltz`` as transformation to ``TIMESTAMP(3)`` from the ``occurred_at`` timestamp in Linux format.
    * the ``WATERMARK`` definition

Example: Define a Flink table using the standard connector over topic in Avro format   
------------------------------------------------------------------------------------

In cases when target of the Flink data pipeline needs to write in Avro format to a topic named  ``metric-topic-tgt`` within the Aiven for Apache Kafka service named ``demo-kafka``.

We can define a ``metrics-out`` Flink table with:

* ``demo-kafka`` as integration service
* ``metric-topic-tgt`` as Apache Kafka topic name
* **Apache Kafka SQL Connector** for the standard connection mode
* **Confluent Avro** as Key data format
* `hostname` as field to be used as key, the key in Apache Kafka is by default used for partition selection 
* **Confluent Avro** as Value data format
* ``metrics-out`` as Flink table name
* The following as SQL schema

.. code:: sql 

    cpu VARCHAR,
    hostname VARCHAR,
    usage DOUBLE

.. Note::

    The SQL schema includes the output message fields ``cpu``, ``hostname``, ``usage`` and the related `data type <https://nightlies.apache.org/flink/flink-docs-release-1.15/docs/dev/table/types/#list-of-data-types>`_.


Example: Define a Flink table using the upsert connector over topic in Avro format   
------------------------------------------------------------------------------------

In cases when target of the Flink pipeline needs to write in Avro format and upsert mode to a compacted topic named  ``metric-topic-tgt`` within the Aiven for Apache Kafka service named ``demo-kafka``.

We can define a ``metrics-out`` Flink table with:

* ``demo-kafka`` as integration service
* ``metric-topic-tgt`` as Apache Kafka topic name
* **Upsert Kafka SQL Connector** for the changelog mode
* **Confluent Avro** as Key data format

.. Note::

    Unlikely the standard Apache Kafka SQL connector, when using the Upsert Kafka SQL connector the key fields are not defined. They are derived by the `PRIMARY KEY` definition in the SQL schema.

* **Confluent Avro** as Value data format
* ``metrics-out`` as Flink table name
* The following as SQL schema

.. code:: sql 

    cpu VARCHAR,
    hostname VARCHAR,
    max_usage DOUBLE,
    PRIMARY KEY (cpu, hostname) NOT ENFORCED

.. Note::

    The SQL schema includes:
    
    * the output message fields ``cpu``, ``hostname``, ``max_usage`` and the related `data type <https://nightlies.apache.org/flink/flink-docs-release-1.15/docs/dev/table/types/#list-of-data-types>`_.
    * the ``PRIMARY KEY`` definition, driving the key part of the Apache Kafka message
