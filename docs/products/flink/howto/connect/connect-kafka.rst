Create a Kafka based Apache Flink table
==============================================

To create a Flink table based on Aiven for Apache Kafka via Aiven console:

1. Navigate to the Aiven for Apache Flink service page, and open the **Jobs and Data** tab.

2. Select the **Data Tables** sub-tab and select the Aiven for Apache Kafka integration to use.

3. Select the connector type and data formats.

   For more information on the connector types and the requirements for each of them, see :doc:`this article </docs/products/flink/concepts/kafka_connectors>`.

4. Define the Flink table **Name**, the source **Kafka topic** and **Schema SQL**.

**Example**: Define a Flink table named ``KCpuIn`` pointing to a Kafka topic named ``cpuIn`` available in the Aiven for Apache Kafka service named ``kafka-devportal-example``

Settings:

* ``kafka-devportal-example`` as the selected service 
* ``KCpuIn`` as **Name**
* ``cpuIn`` as **Kafka topic**
* ``node INT, occurred_at TIMESTAMP_LTZ(3), cpu_in_mb FLOAT`` as **SQL schema**

The image below shows the Aiven console page with the filled details.

.. image:: /images/products/flink/create-table-topic.png
  :scale: 70 %
  :alt: Image of the Aiven for Apache Flink Jobs and Data tab when creating a Flink table on top of an Aiven for Apache Kafka topic


The Flink table for the sink **Kafka topic** could be defined in a similar way

Settings:

* ``kafka-devportal-example`` as the selected service
* ``KAlert`` as **Name**
* ``alert`` as **Kafka topic**
* ``node INT, occurred_at TIMESTAMP_LTZ(3), cpu_in_mb FLOAT`` as **SQL schema**

**Note**: It is possible to have sink **Kafka topic** automatically created by enabling in Kafka ``kafka.auto_create_topics_enable`` in **Advanced configuration** section