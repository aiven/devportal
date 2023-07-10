Set up an Apache Kafka® MirrorMaker 2 replication flow
======================================================

Apache Kafka® MirrorMaker 2 **replication flows** enable the topics sync from a source Apache Kafka® cluster to a target Apache Kafka cluster deployed anywhere in the world. Replication flows can be defined against Aiven for Apache Kafka services or external :doc:`Apache Kafka clusters <integrate-external-kafka-cluster>`.


Set up an Apache Kafka® MirrorMaker 2 replication flow using Aiven console
--------------------------------------------------------------------------

To define a replication flow between a source Apache Kafka cluster and a target cluster:

1.  Log in to the `Aiven Console <https://console.aiven.io/>`_ and select the **Aiven for Apache Kafka MirrorMaker 2** service where you want to define the replication flow.

.. Note::

    If no Aiven for Apache Kafka MirrorMaker 2 are already defined, :doc:`you can create one in the Aiven console <../getting-started>`.

2. In the service **Overview** screen, scroll to the **Service integrations** section and select **Manage integrations**.

3. If there is no integration for the source/target Apache Kafka cluster, follow these steps to set up the necessary integrations:
   
  * On the Integrations screen, choose the desired integration from the list for the source Apache Kafka cluster.
  * Select an existing Apache Kafka service you want to use as the source/target for the replication flow.
  * Provide a cluster alias name (e.g., source-Kafka) to the integration of the Apache Kafka cluster.
  * Repeat the above steps to set up the integration for the target Apache Kafka cluster and provide a cluster alias name.

4. Once that the source and target Apache Kafka clusters are configure, select **Replication flows** from the left sidebar. 

5. Select **Create replication flow**. 

6. On the Create new replication flow screen, define the replication source and target cluster, the :doc:`list of topics to be included or excluded <../concepts/replication-flow-topics-regex>` and the sync settings. 

7. Select **Create**.

8.  In the target Apache Kafka cluster, verify the replicated topics with the topic name  ``source-cluster-alias.source-topic-name``.
