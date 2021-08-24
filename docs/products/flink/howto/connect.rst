Create Flink integrations
===================================

Apache Flink can create streaming data pipelines across services.

Create an integration from Flink
--------------------------------

The integration between Flink and other Aiven services can be created using :doc:`the Aiven cli</docs/tools/cli>`

**Example:** Create an integration between an Aiven for Flink cluster named ``flink-demo`` and an Aiven for Kafka cluster named ``kafka-demo``.

::

  avn service integration-create    \
    --project test                  \
    -t flink                        \
    -s kafka-demo                   \
    -d flink-demo

The integration id, required for the following steps can be fetched with::

    avn service integration-list --project test flink-demo

Create Flink source and sink tables definition via REST-apis
------------------------------------------------------------

Apache Flink requires topics or tables to `be mapped <https://ci.apache.org/projects/flink/flink-docs-release-1.13/docs/dev/table/sql/create/#create-table>`_ before building the related pipelines.
This functionality can be achieved via REST APIs. 

Follow the documentation to check how source and sink tables can be defined on top of:

* :doc:`Apache Kafka topics <connect/connect-kafka.rst>`
* :doc:`Postgresql tables <connect/connect-pg.rst>`




