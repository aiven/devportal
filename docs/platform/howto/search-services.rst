Search for services in Aiven Console
====================================

On the **Current services** page in `Aiven Console <https://console.aiven.io/>`_ you can search for services by keywords and narrow down the results using filters.

Search by keyword
------------------

When you search by keyword, Aiven Console will show all services that have the matching words in the service name, plan, cloud provider, and tags.

Filter search results
----------------------

You can narrow down your search results by clicking **Filter list** and selecting the services, statuses, and providers to filter by.

You can also add filters to the search field yourself. The supported filters are:

* ``service``
* ``status``
* ``provider``
* ``region``

You can add multiple values to filters separated by a comma. For example, this is how you would view all running PostgreSQL services that are hosted on AWS or Google Cloud::

    service:pg status:running provider:aws,google

You can use these filters alongside keyword searches. For example, to see all powered off Kafka services with "production" in the name you could use::

    production service:kafka status:poweroff 


Filter by service type
~~~~~~~~~~~~~~~~~~~~~~~

To filter the services by service type, use the filter values in this table.

.. list-table::
    :align: left
    :widths: 50 25
    :header-rows: 1

    * - Service name
      - Filter value
    * - Cassandra®
      - ``cassandra`` 
    * - ClickHouse®
      - ``clickhouse``
    * - Flink®
      - ``flink``
    * - Grafana®
      - ``grafana``
    * - InfluxDB®
      - ``influxdb``
    * - Kafka®
      - ``kafka``
    * - M3DB®
      - ``m3db``
    * - M3 Aggregator®
      - ``m3aggregator`` 
    * - M3 Coordinator®
      - ``m3coordinator``
    * - MySQL®
      - ``mysql`` 
    * - OpenSearch®
      - ``opensearch`` 
    * - PostgreSQL®
      - ``pg`` 
    * - Redis®
      - ``redis``  


Filter by status
~~~~~~~~~~~~~~~~~
You can filter the services to show only those that are running, powered off, rebuilding, or rebalancing. The values supported for the ``status`` filter are:

* ``running``
* ``poweroff``
* ``rebuilding``
* ``rebalancing``


Filter by cloud provider
~~~~~~~~~~~~~~~~~~~~~~~~

To filter the services by the cloud provider they are hosted on, use the filter values in this table.

.. list-table::
    :align: left
    :widths: 50 25
    :header-rows: 1

    * - Cloud provider
      - Filter value
    * - Amazon Web Services (AWS)
      - ``aws``
    * - Azure
      - ``azure``
    * - Digital Ocean
      - ``do``
    * - Google Cloud Provider (GCP)
      - ``google``
    * - Exoscale
      - ``exoscale``
    * - UpCloud
      - ``upcloud``
    * - Vultr
      - ``vultr``


Filter by cloud region
~~~~~~~~~~~~~~~~~~~~~~~

The supported values for the ``region`` filter are in the **Cloud** column of the tables on the :doc:`List of available cloud regions </docs/platform/reference/list_of_clouds>` page. For example, to see all services in the AWS ``eu-central-1`` region you would use this filter::

    region:aws-eu-central-1