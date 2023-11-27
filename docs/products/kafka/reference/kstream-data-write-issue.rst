Resolving data write issue on Apache Kafka® Streams 3.6.0
=========================================================

Issue description
------------------
If you get the ``UNKNOWN_SERVER_ERROR`` error while generating data using Apache Kafka® Streams **version 3.6.0**, it may result in data write issues.
and errors in broker logs such as:

.. code-block:: bash

    "Error processing append operation on partition XXXX (kafka.server.ReplicaManager) java.lang.NullPointerException."

This issue is known to the Apache Kafka® project. See `Kafka-15653 <https://issues.apache.org/jira/browse/KAFKA-15653>`_.

Solution
--------

- **Recommended solution:** It is recommended to upgrade your Apache Kafka® Streams clients to **version 3.6.1**.
- **Alternative solution:** Alternatively, in case of a failure requiring an immediate fix, users
  can set the ``transaction_partition_verification_enable`` parameter to ``false`` under advanced configuration of the service. This allows Kafka to accept messages despite the existing bug.

  .. Important::
     When you can update to 3.6.1, do not forget to set ``transaction_partition_verification_enable`` to ``true``.

If the issue persists even after trying these solutions, reach out to our support team.