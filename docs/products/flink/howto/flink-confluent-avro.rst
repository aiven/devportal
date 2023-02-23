Create Confluent Avro-based Apache Flink® table 
=================================================

`Confluent Avro <https://nightlies.apache.org/flink/flink-docs-release-1.16/docs/connectors/table/formats/avro-confluent/>`_ is a format that supports schema registry, allowing for data serialization and deserialization in a language-agnostic, easy-to-read format that supports schema evolution.

Aiven for Apache Flink® simplifies the process of creating an Apache Flink® source table that uses the Confluent Avro data format with Karapace, an open-source schema registry for Apache Kafka® that enables you to store and retrieve Avro schemas. With Aiven for Apache Flink, you can stream data in the Confluent Avro data format and perform real-time transformations. 

This article provides information on how to create an Apache Flink source table that uses Confluent Avro to stream Avro messages.


Prerequisites
--------------

* :doc:`Aiven for Apache Flink service </docs/platform/howto/create_new_service>` with Aiven for Apache Kafka® integration. See :doc:`/docs/products/flink/howto/create-integration` for more information.  
* Aiven for Apache Kafka® service with Karapace Schema registry enabled. See :doc:`/docs/products/kafka/karapace/getting-started` for more information.  

Create an Apache Flink® table with Confluent Avro
--------------------------------------------------

1. In the Aiven for Apache Flink® service page, open the **Application** tab.
2. Create a new application or select an existing one with Aiven for Apache Kafka® integration.

   .. note:: 
    If editing an existing application, create a new version to make changes to the source or sink tables.

3. In the **Create new version** screen, click **Add source tables**.
4. Click **Add new table** or click **Edit** if you want to edit an existing source table. 
5. In the **Add new source table** or **Edit source table** screen, select the Aiven for Apache Kafka® service as the integrated service. 
6. In the **Table SQL** section, enter the SQL statement below to create an Apache Kafka®-based Apache Flink® table with Confluent Avro: 
   
.. code:: sql

    CREATE TABLE kafka (
      
    ) WITH (
      'connector' = 'kafka',
      'properties.bootstrap.servers' = '',
      'scan.startup.mode' = 'earliest-offset',
      'topic' = 'my_test.public.students',
      'value.format' = 'avro-confluent'
      'avro-confluent.url' = 'http://localhost:8082',
      "value.avro-confluent.basic-auth.credentials-source" = 'USER_INFO'
      "value.avro-confluent.basic-auth.user-info" = 'user_info'
    )

The following are the parameters:

*  ``connector``: the **Kafka connector type**, between the **Apache Kafka SQL Connector** (value ``kafka``) for standard topic reads/writes and the **Upsert Kafka SQL Connector** (value ``upsert-kafka``) for changelog type of integration based on message key. 
   
   .. note::
    For more information on the connector types and the requirements for each, see the articles on :doc:`Kafka connector types </docs/products/flink/concepts/kafka-connectors>` and :doc:`the requirements for each connector type </docs/products/flink/concepts/kafka-connector-requirements>`.

* ``properties.bootstrap.servers``: this parameter can be left empty since the connection details will be retrieved from the Aiven for Apache Kafka integration definition

* ``topic``: the topic to be used as a source for the data pipeline. If you want to use a new topic that does not yet exist, write the topic name.

  .. Warning::
    By default, Flink will not be able to create Apache Kafka topics while pushing the first record automatically. To change this behavior, enable in the Aiven for Apache Kafka target service the ``kafka.auto_create_topics_enable`` option in **Advanced configuration** section.

* ``value.format``:  indicates that the value data format is in the Confluent Avro format.
* ``avro-confluent.url``: this is the URL for the Karapace schema registry.
* ``value.avro-confluent.basic-auth.credentials-source``: this specifies the source of the user credentials for accessing the Karapace schema registry. It should be set to USER_INFO.
* ``value.avro-confluent.basic-auth.user-info``: this should be set to the ``user_info`` string you created earlier. 
   
  .. important:: 
    The ``user_info`` is a string that contains the username and password for the Karapace schema registry user in the format of ``user_info = f"{username}:{password}"``. It is important to provide this information to authenticate and access the Karapace schema registry.

7. To create a sink table, click **Add sink tables** and repeat steps 4-6 for sink tables.
8. In the **Create statement** section, create a statement that defines the fields retrieved from each message in a topic.

Example: Define a Flink table using the standard connector over topic in Confluent Avro format
-----------------------------------------------------------------------------------------------

The Aiven for Apache Kafka service called ``demo-kafka`` includes a topic called ``my_test.public.student`` that holds a stream of student data in Confluent Avro format like:

.. code:: text

  {"id": 1, "name": "John", "email": "john@gmail.com"}
  {"id": 2, "name": "Jane", "email": "jane@yahoo.com"}
  {"id": 3, "name": "Bob", "email": "bob@hotmail.com"}
  {"id": 4, "name": "Alice", "email": "alice@gmail.com"}

You can define a ``students`` Flink table by selecting ``demo-kafka`` as the integration service and writing the following SQL schema:

.. code:: 
  
    CREATE TABLE students (
      id INT,
      name STRING,
      email STRING
      ) WITH (
      'connector' = 'kafka',
      'properties.bootstrap.servers' = '',
      'scan.startup.mode' = 'earliest-offset',
      'topic' = 'my_test.public.students',
      'value.format' = 'avro-confluent'
      'avro-confluent.url' = 'http://localhost:8082',
      'value.avro-confluent.basic-auth.credentials-source'= 'USER_INFO',
      'value.avro-confluent.basic-auth.user-info" = 'user_info',
    )


.. Note::

    The SQL schema includes the output message fields ``id``, ``name``, ``email`` and the related `data type <https://nightlies.apache.org/flink/flink-docs-release-1.16/docs/dev/table/types/#list-of-data-types>`_.
