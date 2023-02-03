Create a DataGen-based Apache Flink® table
===========================================

The DataGen source table is a built-in connector of the Apache Flink system that generates random data periodically, matching the specified data type of the source table. This section provides you with information on how to connect DataGen as a source table in an Aiven for Apache ®Flink application.

Configure Datagen as source for Flink application
-------------------------------------------------
To configure DataGen as the source using the DataGen build-in connector for Apache Flink, follow these steps: 

1. In the Aiven for Apache Flink service page, open the **Application** tab.
2. Create a new application or select an existing application for your desired :doc:`data service integration <../howto/create-integration>`. 

.. note:: 
    If you are editing an existing application, you need to create a new version of the application to make changes to the source or sink table.

3. In the **Create new version** screen, click **Add source tables**.
4. Click **Add new table** or click **Edit** if you want to edit an existing source table. 
5. In the **Add new source table** or **Edit source table** screen, select the Aiven for Apache Kafka service as the integrated service. 
6. In the **Table SQL** section, enter the SQL statement below to create the Apache Kafka-based Apache Flink:

   ::

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
        
7. To create a sink table, click **Add sink tables** and repeat steps 4-6 for sink tables.
8. In the **Create statement** section, create a statement that defines the fields retrieved from each message in a topic, additional transformations such as format casting or timestamp extraction, and :doc:`watermark settings <../concepts/watermarks>`. 

