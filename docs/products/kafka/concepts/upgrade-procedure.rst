Apache Kafka® upgrade procedure
===============================

One of the benefits of using a managed service like Aiven for Apache Kafka® is the automated upgrade procedure. 

The upgrade procedure is executed during:
    
* maintenance updates
* plan changes
* cloud region migrations
* manual node replacements performed by an Aiven operator
    
All the above operations involve creating new broker nodes to replace existing ones.

Upgrade procedure steps
---------------------------

To demonstrate what steps are taken during the automated upgrade procedure, we'll look at the example for a 3-node Apache Kafka service visualised below:

.. mermaid::

    flowchart TD;
        subgraph KafkaCluster
            subgraph Node1
                PartitionA1([Partition A])
                PartitionB1([Partition B])
            end
            subgraph Node2
                PartitionA2([Partition A])
                PartitionC1([Partition C])
            end
            subgraph Node3
                PartitionB2([Partition B])
                PartitionC2([Partition C])
            end
            
            
        end
        
The following set of steps are executed during an upgrade procedure:    

1. New Apache Kafka® nodes are started alongside the existing nodes

2. Once the new nodes are running, they join the Apache Kafka cluster

.. Note::
    The Apache Kafka cluster now contains a mix of old and new nodes       

3. The partition data and leadership is transferred to new nodes

.. mermaid::

    flowchart TD;

        subgraph KafkaCluster
            subgraph Node1
                PartitionA1([Partition A])
                PartitionB1([Partition B])
            end
            subgraph Node2
                PartitionA2([Partition A])
                PartitionC1([Partition C])
            end
            subgraph Node3
                PartitionB2([Partition B])
                PartitionC2([Partition C])
            end
            subgraph NewNode1
                PartitionNewA1([Partition A])
                PartitionNewC1([Partition C])
            end
            subgraph NewNode2
                PartitionNewB1([Partition B])
                PartitionNewC2([Partition C])
            end
            subgraph NewNode3
                PartitionNewA2([Partition A])
                PartitionNewB2([Partition B])
            end
        end

        PartitionA1 -.-> PartitionNewA1
        PartitionB1 -.-> PartitionNewB1
        PartitionC1 -.-> PartitionNewC1
        PartitionA2 -.-> PartitionNewA2
        PartitionB2 -.-> PartitionNewB2
        PartitionC2 -.-> PartitionNewC2

.. Warning::

    This step is CPU intensive due to the additional data movement overhead.

4. Once old nodes don't have any partition data, they are retired from the cluster.
        
.. Note::

    Depending on the cluster size more new nodes are added (by default up to 6 nodes at a time are replaced)



5. The process is completed once the last old node has been removed from the cluster

.. mermaid::

    flowchart TD;

        subgraph KafkaCluster
            subgraph NewNode1
                PartitionNewA1([Partition A])
                PartitionNewC1([Partition C])
            end
            subgraph NewNode2
                PartitionNewB1([Partition B])
                PartitionNewC2([Partition C])
            end
            subgraph NewNode3
                PartitionNewA2([Partition A])
                PartitionNewB2([Partition B])
            end
        end

Zero upgrade downtime
---------------------

The upgrade process described above has no downtime, since there always be active nodes in cluster and the same service URI will resolve to all the active nodes. But, since the upgrade generates extra load during the transfer of partitions, the overall cluster performance can slow down or even prevent the progress of normal work if the cluster is already under heavy load.

Apache Kafka client trying to produce or consume messages might face warning ``leader not found`` messages as the partitions are moved between brokers. This is normal and most client libraries handle this automatically but the warnings may look alarming in the logs, to understand more read the :doc:`dedicated document <non-leader-for-partition>`. 

Upgrade duration
----------------

The upgrade duration can vary quite significantly and depends on:

* The amount of data stored in the cluster
* The number of partitions: each partition represents an overhead since also partition leadership needs to be moved to the new nodes
* The spare resources available on the cluster: if the cluster is already under heavy load, the resources dedicated to the upgrade procedure will be minimal

To achieve quicker upgrades, Aiven therefore recommends running the procedure during low periods of low load to reduce the overhead of producers and consumers. If a service is already tightly constrained on resources, it is recommend to disable all non-essential usage during the upgrade to allow more resources to be used on coordinating and moving data between nodes.

Upgrade rollback
----------------

Rollback is not available since old nodes are deleted once they are removed from the cluster. 

.. Note::

    Nodes are not removed from the cluster while they hold data. If an upgrade doesn't progress, the nodes are not removed since that would lead to data loss. 
    
In case of an upgrade procedure due to a plan change, the old plan can be restored via the :doc:`Aiven Console </docs/platform/howto/scale-services>` or the :ref:`Aiven CLI <avn-cli-service-update>`.

Upgrade impact and risks
------------------------

During the upgrade procedure additional CPU load is generated by partition leadership coordination and streaming data to new nodes. To mitigate the risk run the upgrade at a time of low traffic and/or reduce the normal workload on the cluster by disabling non-essential producers and consumers.

Specifically when upgrading to a smaller plan, the disk could reach the :doc:`maximum allowed limit </docs/products/kafka/howto/prevent-full-disks>` which can prevent progress of the procedure. To mitigate the risk check the disk usage before the upgrade and evaluate the amount of space left. 

.. Note::

    In case of emergency, our operations team is able to help by adding additional volumes to the old nodes temporarily.