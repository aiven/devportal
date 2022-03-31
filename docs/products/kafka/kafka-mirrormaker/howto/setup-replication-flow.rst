Set up an Apache Kafka® MirrorMaker 2 replication flow
======================================================

Apache Kafka® MirrorMaker 2 **replication flows** enable the topics sync from a source Apache Kafka® cluster to a target Apache Kafka cluster deployed anywhere in the world. Replication flows can be defined against Aiven for Apache Kafka services or external :doc:`Apache Kafka clusters <integrate-external-kafka-cluster>`.


Set up an Apache Kafka® MirrorMaker 2 replication flow using Aiven console
--------------------------------------------------------------------------

To define a replication flow between a source Apache Kafka cluster and a target cluster:

1. Navigate to the `Aiven Console <https://console.aiven.io/>`_ and select the Aiven for Apache Kafka MirrorMaker 2 service where the replication flow needs to be defined.

.. Note::

    If no Aiven for Apache Kafka MirrorMaker 2 are already defined, :doc:`you can create one in the Aiven console <../getting-started>`.

2. In the **Overview** tab scroll to the **Service Integrations** section and click on **Manage integrations**.

3. If the integration to the source Apache Kafka cluster doesn't yet exist, select the **Kafka MirrorMaker 2** and click on **Use Integration**.

4. Select the Apache Kafka cluster you want to use as source for the replication flow.

5. Provide the Apache Kafka cluster integration an alias name (e.g. ``source-kafka``)

6. Repeat the steps 3. 4. and 5. for the target Apache Kafka cluster if the integration doesn't yet exist.

7. Navigate to the **Replication Flows** tab and click **Create replication flow**

8. Define the replication source and target cluster, the :doc:`list of topics to be included or excluded <../concepts/replication-flow-topics-regex>` and the sync settings, then click on **Create**

9. In the target Apache Kafka cluster, check the replicated topics having topic name ``source-cluster-alias.source-topic-name``
