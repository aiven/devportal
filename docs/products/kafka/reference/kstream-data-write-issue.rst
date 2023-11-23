Resolving data write issue on Apache Kafka® Streams 3.6.0
=========================================================

Issue description
------------------
If you are encountering an ``UNKNOWN_SERVER_ERROR`` while producing data using Apache Kafka® Streams version 3.6.0, it may result in the prevention of data writing. This issue has been identified and logged in the Apache Kafka® project's issue tracker with the reference: `Kafka-15653 <https://issues.apache.org/jira/browse/KAFKA-15653>`_.

This could lead to errors in broker logs as,

.. code-block:: bash

    "Error processing append operation on partition XXXX (kafka.server.ReplicaManager) java.lang.NullPointerException."


Solution
--------
To address this issue, it is recommended to upgrade your Apache Kafka® Streams clients to version 3.6.1. This version contains the necessary fixes to resolve the ``UNKNOWN_SERVER_ERROR``.


.. Note::
    If the issue persists even after upgrading Apache Kafka® Streams to 3.6.1 version, please reach out to our support team for further assistance.