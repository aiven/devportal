Scaling options in Apache Kafka®
================================

Aiven for Apache Kafka® has a number of predefined plans that specify the
number of brokers and the capacity of individual brokers. The predefined plans consist of 3, 6, 9, 15, or 30 brokers, but we can also create
larger custom plans based on customer requirements.

To increase the capacity of an existing Kafka cluster, two options are
available:

* **Vertical** scaling the performance of individual brokers

* **Horizontal** scaling the cluster by adding more brokers

Both scaling options are available for all Aiven for Apache Kafka customers and don't require any downtime, keeping your cluster up and running during the upgrade. 

.. Note::

    When you change the service plan, Aiven automatically starts adding new brokers with the new specifications to your existing cluster. Once the new brokers are online and the data is replicated to them from the older nodes, the old brokers are retired one by one.

Aiven recommends to use both the vertical and horizontal scaling capabilities of Aiven for Apache Kafka to achieve the best possible performance and fault tolerance. 

.. Tip::

    For production clusters, Aiven advises a minimum of 6 cluster nodes to avoid situations when a failure in a single cluster node causes a sharp increase in load for the remaining nodes.


Vertical scaling
----------------

Scaling vertically a Kafka cluster means keeping the same number of brokers but replacing existing nodes with higher capacity nodes. 
If you cannot increase the partition or topic count of your Kafka cluster due to application constraints, this is usually the only available option.

An example of vertical scaling is when changing the service plan from **Aiven for Apache Kafka Business-4** to **Aiven for Apache Kafka Business-8**. For such case Aiven immediately launches three new brokers with the increased capacity defined by the **Business-8** plan, transfers the data in the new nodes, and once the data is replicated retires the old brokers.

Horizontal scaling
--------------------

Scaling horizontally means adding more brokers to an existing Kafka cluster. This allows sharing the load in the cluster between a larger number of individual nodes, allowing the cluster to serve more requests as a whole.

.. Note::

    Scaling horizontally also makes the cluster more resilient to a failure of a single node: if one broker in a 3-node cluster fails, the remaining two nodes get a 50% load increase, which may cause availability issues in the cluster. If one broker in a 9-node cluster fails, the remaining 8 nodes will only see a load increase of roughly 13%.

An example of horizontal scaling is changing the service from the 3-node **Aiven for Apache Kafka Business-8** plan to the 6-node *Aiven for Apache Kafka Premium-6x-8* plan. For such case, Aiven immediately launches six new brokers adding them to the existing cluster. The existing cluster nodes stay online, and once the new brokers are online and included in the cluster configuration, Kafka starts placing partition replicas on them. 
Once all the data is copied to the new brokers the old nodes are removed. 

.. Warning::
    
    Depending on the data volumes, it may take some time until the Apache Kafka cluster is fully balanced.
