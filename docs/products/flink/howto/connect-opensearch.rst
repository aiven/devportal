Create an OpenSearch®-based Apache Flink® table
===============================================

To build data pipelines, Apache Flink® requires you to map source and target data structures as `Flink tables <https://nightlies.apache.org/flink/flink-docs-stable/docs/dev/table/sql/create/#create-table>`_ within an application. You can accomplish this through the `Aiven Console <https://console.aiven.io/>`_ or :doc:`Aiven CLI </docs/tools/cli/service/flink>`.

You can define a Flink table over an existing or new Aiven for OpenSearch® index, to sink streaming data. To define a table over an OpenSearch® index, specify the index name, column data formats, and the Flink table name you want to use as a reference when building data pipelines.

.. Warning:: 

    * To use Flink tables an :doc:`existing integration <create-integration>` must be available between the Aiven for Flink® service and one or more Aiven for OpenSearch® services.
    * You can use Aiven for OpenSearch® can only as the **target** of a data pipeline. You can create Flink applications that write data to an OpenSearch® index. However, reading data from an OpenSearch® index is currently not possible.


Create an OpenSearch®-based Apache Flink® table with Aiven Console
------------------------------------------------------------------

To create an Apache Flink table based on an Aiven for OpenSearch® index via Aiven console:

1.  In the Aiven for Apache Flink service page, select **Application** from the left sidebar.

2. Create a new application or select an existing one with Aiven for OpenSearch® integration.
    
   .. note:: 
     
      If editing an existing application, create a new version to make changes to the source or sink tables.

3. In the **Create new version** screen, select **Add sink tables**.

4. Select **Add new table** or select **Edit** if you want to edit an existing source table. 

5. In the **Add new sink table** or **Edit sink table** screen, select the Aiven for OpenSearch® as the integrated service. 

6. In the **Table SQL** section, enter the SQL statement to create the OpenSearch-based Apache Flink table. 

   * Define the **Flink table name**, which will represent the Flink reference to the topic and will be used during the data pipeline definition.

7. In the **Create statement** section, write the SQL schema that defines the fields to be pushed for each message in the OpenSearch index.

Example: Define an Apache Flink® table to OpenSearch®
-----------------------------------------------------

We want to push the result of an Apache Flink® application to an index named  ``metrics`` in an Aiven for OpenSearch® service named ``demo-opensearch``. The application result should generate the following data:

.. code:: text

    {'hostname': 'sleepy', 'cpu': 'cpu3', 'usage': 93.30629927475789, 'occurred_at': 1637775077782}
    {'hostname': 'dopey', 'cpu': 'cpu4', 'usage': 88.39531418706092, 'occurred_at': 1637775078369}
    {'hostname': 'happy', 'cpu': 'cpu2', 'usage': 77.90860728236156, 'occurred_at': 1637775078964}
    {'hostname': 'dopey', 'cpu': 'cpu4', 'usage': 81.17372993952847, 'occurred_at': 1637775079054}

We can define a ``metrics_out`` Apache Flink® table with:

* ``demo-opensearch`` as integration service
* ``metrics`` as OpenSearch® index name
* ``metrics_out`` as Flink table name
* the following as SQL schema

.. code:: sql 

    CREATE TABLE metrics_out (
    cpu VARCHAR,
    hostname VARCHAR,
    usage DOUBLE,
    occurred_at BIGINT
    ) WITH (
    'connector' = 'elasticsearch-7',
    'hosts' = '',
    'index' = 'metrics'
    )

The ``hosts`` will be substituted with the appropriate address during runtime.