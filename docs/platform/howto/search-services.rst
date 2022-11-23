Search for services in Aiven Console
====================================

On the **Current services** page in `Aiven Console <https://console.aiven.io/>`_ you can search for services by keywords and narrow down the results using filters.

Search by keyword
------------------

When you search by keyword, Aiven Console will show all services that have the maching words in the service name, plan, cloud, and tags.

Filter search results
----------------------

You can narrow down your search results by clicking **Filter list** and selecting the services, statuses, and providers to filter.

You can also add filters to the search box yourself. The supported filters are:

* ``service``
* ``status``
* ``provider``
* ``region``

For example, to filter the services to show all running PostgreSQL services that are hosted on AWS or Google Cloud::

    service:pg status:running provider:aws,google

You can use these filters alongside keywords. For example::

    prod service:kafka status:poweroff provider:google,azure


Filter by service type
~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :align: left
    :widths: 50 25
    :header-rows: 1

    * - Service name
      - Filter value
    * - Cassandra
      - cassandra 
    * - ClickHouse
      - clickhouse
    * - Flink
      - flink
    * - Grafana
      - grafana
    * - InfluxDB
      - influxdb
    * - Kafka
      - kafka   
    * - M3DB
      - m3db
    * - M3 Aggregator
      - m3aggregator 
    * - M3 Coordinator
      - m3coordinator
    * - MySQL
      - mysql 
    * - OpenSearch
      - opensearch 
    * - PostgreSQL
      - pg 
    * - Redis
      - redis  




Filter by status
~~~~~~~~~~~~~~~~~
The values supported for the ``status`` filter are:

* running
* poweroff
* rebuilding
* rebalancing

Filter by cloud provider
~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table::
    :align: left
    :widths: 50 25
    :header-rows: 1

    * - Cloud provider
      - Filter value
    * - Amazon Web Services (AWS)
      - aws 
    * - Azure
      - azure 
    * - Digital Ocean
      - do 
    * - Google Cloud Provider (GCP)
      - google
    * - Exoscale
      - exoscale 
    * - UpCloud
      - upcloud 
    * - Vultr
      - vultr

Filter by cloud region
~~~~~~~~~~~~~~~~~~~~~~~

The supported values for the ``region`` filter are on the :doc:`List of available cloud regions </docs/platform/reference/list_of_clouds>` page. For example, to see all services in the AWS region eu-central-1 you would use this filter::

    region:aws-eu-central-1


