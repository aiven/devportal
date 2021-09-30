Connect Flink to other services via table definition
-----------------------------------------------------

To build data pipelines, Apache Flink requires source or target data structures to `be mapped as Flink tables <https://ci.apache.org/projects/flink/flink-docs-release-1.13/docs/dev/table/sql/create/#create-table>`_.
This functionality can be achieved via REST APIs or Aiven console. 

Follow the dedicated documentation to check how Aiven for Apache Flink tables can be defined on top of:

* :doc:`Aiven for Apache Kafka topics <connect/connect-kafka>`
* :doc:`Aiven for Postgresql tables <connect/connect-pg>`