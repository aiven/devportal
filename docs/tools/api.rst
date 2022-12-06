Aiven API
=========

Use the Aiven API to programmatically perform any task that you can do through the web interface. This is an ideal way to automate tasks involving Aiven at every stage of your workflow.

Common use cases for the Aiven API:

* Use with CI (Continuous Integration) to spin up data platforms on Aiven for use during test runs.

* Integrate with other parts of your existing automation setup to achieve complex tasks.

* Deploy and tear down development or demo platforms on a schedule.

We make the API available to all Aiven users. It is also the engine behind the Aiven Console, so you should find that all operations are also available through the API.


API quickstart
--------------

* **Postman**: Try `Aiven on Postman <https://www.postman.com/aiven-apis/workspace/aiven/documentation/21112408-1f6306ef-982e-49f8-bdae-4d9fdadbd6cd>`_ and start working with your data platform programmatically.

* **API documentation**: Check the `API documentation and OpenAPI description <https://api.aiven.io/doc/>`_ to work with the API directly.

* **Examples**: See the API in action with some :doc:`api/examples`.

Authentication
--------------

Most (but not all) endpoints require authentication. You'll need an authentication token from the `profile section of your Aiven console <https://console.aiven.io/profile/auth>`_.

Send this token in the header, using a structure like this, and replacing ``TOKEN`` with your actual API token::

    Authorization: aivenv1 TOKEN

Read more about :doc:`/docs/platform/concepts/authentication-tokens`.

Handling JSON responses
-----------------------

The `Aiven API <https://api.aiven.io/doc/>`_ returns information in JSON format, sometimes a lot of
information. This is perfect for machines but not ideal for humans. Try a tool
like ``jq`` (https://stedolan.github.io/jq/) to make things easier to read and
manipulate.

Per-service configuration
-------------------------

Many of the API endpoints allow additional configuration that varies depending on the type of service you are using. Check out the documentation for each service to see the configuration options available:

* :doc:`Apache Kafka configuration</docs/products/kafka/reference/advanced-params>`
* :doc:`PostgreSQL configuration </docs/products/postgresql/reference/list-of-advanced-params>`
* :doc:`Apache Flink configuration </docs/products/flink/reference/advanced-params>`
* :doc:`ClickHouse configuration </docs/products/clickhouse/reference/advanced-params>`
* :doc:`OpenSearch configuration </docs/products/opensearch/reference/advanced-params>`
* :doc:`M3DB configuration </docs/products/m3db/reference/advanced-params>`
* :doc:`MySQL configuration </docs/products/mysql/reference/advanced-params>`
* :doc:`Redis configuration </docs/products/redis/reference/advanced-params>`
* :doc:`Apache Cassandra configuration </docs/products/cassandra/reference/advanced-params>`
* :doc:`Grafana configuration </docs/products/grafana/reference/advanced-params>`
* :doc:`InfluxDB configuration </docs/products/influxdb/reference/advanced-params>`

Further reading
---------------

Here are some more resources for you:

* Some `API examples on the Aiven blog <https://aiven.io/blog/your-first-aiven-api-call>`_. This post also includes information about importing our OpenAPI description into Postman.
* Learn more about the :doc:`/docs/tools/cli`.
