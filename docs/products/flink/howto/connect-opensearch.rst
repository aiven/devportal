Create an OpenSearch®-based Apache Flink® table
===============================================

To build data pipelines, Apache Flink® requires source and target data structures to `be mapped as Flink tables <https://ci.apache.org/projects/flink/flink-docs-release-1.13/docs/dev/table/sql/create/#create-table>`_. This functionality can be achieved via the `Aiven console <https://console.aiven.io/>`_ or :doc:`Aiven CLI </docs/tools/cli/service/flink>`.

A Flink table can be defined over an existing or new Aiven for OpenSearch® index, to sink streaming data. To define a table over an OpenSearch® index, the index name and column data formats need to be defined, together with the Flink table name to use as reference when building data pipelines.

.. Warning:: 

    Aiven for OpenSearch® can only be used as the **target** of a data pipeline. You'll be able to create jobs that write data to an OpenSearch® index. Reading data from an OpenSearch® index is currently not possible.


Create an OpenSearch®-based Apache Flink® table with Aiven Console
------------------------------------------------------------------

To create an Apache Flink table based on an Aiven for OpenSearch® index via Aiven console:

1. Navigate to the Aiven for Apache Flink® service page, and open the **Jobs and Data** tab.

   .. Warning::

      In order to define Flink's tables an :doc:`existing integration <create-integration>` needs to be available between the Aiven for Flink® service and one or more Aiven for OpenSearch® services.

2. Select the **Data Tables** sub-tab and select the Aiven for OpenSearch® integration to use

3. Select the Aiven for OpenSearch® service and the **index** to be used as target for the data pipeline. If you want to use a new index that does not yet exist, just write the index name and it will be created.

4. Define the **Flink table name**; this name represents the Flink reference to the topic and will be used during the data pipeline definition

5. Define the **SQL schema**: the SQL schema defines the fields pushed for each message in an index

Example: Define an Apache Flink® table to OpenSearch®
-----------------------------------------------------

We want to push the result of an Apache Flink® job to an index named  ``metrics`` in an Aiven for OpenSearch® service named ``demo-opensearch``. The job result should generate the following data:

.. code:: text

    {'hostname': 'sleepy', 'cpu': 'cpu3', 'usage': 93.30629927475789, 'occurred_at': 1637775077782}
    {'hostname': 'dopey', 'cpu': 'cpu4', 'usage': 88.39531418706092, 'occurred_at': 1637775078369}
    {'hostname': 'happy', 'cpu': 'cpu2', 'usage': 77.90860728236156, 'occurred_at': 1637775078964}
    {'hostname': 'dopey', 'cpu': 'cpu4', 'usage': 81.17372993952847, 'occurred_at': 1637775079054}

We can define a ``metrics-out`` Apache Flink® table with:

* ``demo-opensearch`` as integration service
* ``metrics`` as OpenSearch® index name
* ``metrics_out`` as Flink table name
* the following as SQL schema

.. code:: sql 

    cpu VARCHAR,
    hostname VARCHAR,
    usage DOUBLE,
    occurred_at BIGINT

After clicking on the **Create** button, the ``metrics_out`` table should be visible in the table browser