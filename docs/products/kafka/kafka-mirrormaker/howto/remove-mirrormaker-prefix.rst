Remove topic prefix when replicating with Apache Kafka® MirrorMaker 2
======================================================================

When using Apache Kafka® MirrorMaker 2 to replicate topics across Apache Kafka® clusters, the default target topic name is in the form ``<SOURCE_CLUSTER_ALIAS>.<TOPIC_NAME>``.
E.g. if the source Apache Kafka clusters alias is ``src-kafka``, replicating the source topic named ``orders`` via Apache Kafka MirrorMaker 2 creates a target topic named ``src-kafka.orders``.

For most use cases, the extra prefix is not an issue. However, you might be using a backup Apache Kafka cluster for Disaster Recovery. In this scenario, you want your consumers and producers to be able to switch with minimal downtime and without needing to modify the topic names in their configuration.

In such cases, to remove the topic prefix, you'll need to change the replication flow ``replication_policy_class`` parameter from the default ``org.apache.kafka.connect.mirror.DefaultReplicationPolicy`` value which includes the source cluster alias in the target topic name to ``org.apache.kafka.connect.mirror.IdentityReplicationPolicy``.

The change can be performed via the `Aiven console <https://console.aiven.io/>`_ by modifying the flow details in the service page "Replication Flow" tab, or via  :doc:`Aiven CLI </docs/tools/cli>` as described in the following section. 

Remove topic prefix from a replication flow
--------------------------------------------------

To remove the source cluster alias as topic prefix in an existing replication flow via the :doc:`Aiven CLI </docs/tools/cli>` execute the following command, replacing the ``<MIRRORMAKER_SERVICE_NAME>``, ``<SOURCE_CLUSTER_ALIAS>`` and ``<TARGET_CLUSTER_ALIAS>`` placeholders:

::

    avn MirrorMaker replication-flow update <MIRRORMAKER_SERVICE_NAME> \
        --source-cluster <SOURCE_CLUSTER_ALIAS>                         \
        --target-cluster <TARGET_CLUSTER_ALIAS>                         \
        "{\"replication_policy_class\": \"org.apache.kafka.connect.mirror.IdentityReplicationPolicy\"}"    

In case you need to revert the policy and include the source cluster alias as topic prefix, execute the above command passing the ``org.apache.kafka.connect.mirror.DefaultReplicationPolicy`` value.

.. Warning::

    The ``org.apache.kafka.connect.mirror.IdentityReplicationPolicy`` replication policy **doesn't support active-active replication** as the topics keep the same name and offsets can not be accurately tracked. Creating the same replication flows between a source and a destination with ``org.apache.kafka.connect.mirror.IdentityReplicationPolicy`` policy creates an infinite loop. 
    
    For active-active, please use the ``org.apache.kafka.connect.mirror.DefaultReplicationPolicy``.
