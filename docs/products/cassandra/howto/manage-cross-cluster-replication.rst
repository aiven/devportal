Manage cross-cluster replication in Aiven for Apache Cassandra® |beta|
======================================================================

Learn how to update Apache Cassandra® services that has cross-cluster replication (CCR) enabled: change the service plan and add an extra disk space. Find out how to set up the replication factor and the consistency level for your CCR-enabled Apache Cassandra® services.

Prerequisites
-------------

Aiven-wise
''''''''''

* Aiven account
* Pair of Aiven for Apache Cassandra services with CCR enabled

Tools
'''''

* To update the service plan or add an extra disk space, you need the `Aiven console <https://console.aiven.io/>`_.
* To set up the replication factor, you need the ``cqlsh`` Cassandra client.
* To set up the consistency level, you need either the ``cqlsh`` Cassandra client or your client software.

Change the service plan
-----------------------

.. important::

    When you change the plan for your CCR-enabled service, the plan for the connected replica service changes accordingly since the services constituting a CCR pair always share the same service plan.

.. note::
    
    It's recommended to use the `Aiven console <https://console.aiven.io/>`_ for changing the plan for a CCR-enabled service.

1. Log in to the `Aiven console <https://console.aiven.io/>`_.
2. From the **Current services** view, select a CCR-enabled Aiven for Apache Cassandra service that you want to update.
3. In the **Overview** tab of your service's page, navigate to **Service plan** and select **Change plan**.
4. In the **Change service plan** view, select a new plan you want to use for your service.

   .. tip::
      
      You can also add extra disk space for your service by using the slider in the **Additional disk storage** section.

5. Select **Change**.

.. topic:: Result
    
    You've changed the plan for your CCR-enabled service and its CCR-replica service.

Add an extra disk space
-----------------------

.. important::

    Changes to the storage space are applied to both services constituting the CCR pair so also affect the replica service.

.. note::
    
    It's recommended to use the `Aiven console <https://console.aiven.io/>`_ for adding storage space for CCR-enabled services.

1. Log in to the `Aiven console <https://console.aiven.io/>`_.
2. From the **Current services** view, select a CCR-enabled Aiven for Apache Cassandra service that you want to update.
3. In the **Overview** tab of your service's page, navigate to the **Service plan** section and select **Add storage**.
4. In the **Upgrade service storage** view, use the slider to add extra disk space for your service.

   .. tip::
    
      You can also change your service plan by selecting **Change plan** in the **Your current plan** section.

.. topic:: Result
    
    You've added extra disk storage space for your CCR-enabled service and its CCR-replica service.

Set up the replication factor
-----------------------------

You can specify how many replicas of your data you'd like to have on either of datacenters hosting your service.
For that purpose, you need a new keystore where your data can be stored in tables. To create a keystore that supports CCR and defines the replication factor, you need to run the ``CREATE KEYSPACE`` query with a set of parameters configuring the keyspace as needed.

.. note::
    
    This instruction uses the ``cqlsh`` Cassandra CLI client to configure the replication factor.

1. :doc:`Connect to your service via cqlsh </docs/products/cassandra/howto/connect-cqlsh-cli>`.

   .. note::

      You can connect to either of the two services constituting the CCR pair to set up the replication factor.

2. From the ``cqlsh`` shell, check out
   
   * Existing keyspaces with the ``DESCRIBE keyspaces;`` query (for a new service, only system keyspaces are returned)
   * Datacenters available for your service with the ``SELECT data_center from system.peers_v2;`` query.

3. Create a keyspace by running a query in which you specify

   * Replication strategy (``'class': 'NetworkTopologyStrategy'``)
   * Number of replicas to be created in the first datacenter (``'datacenter_1_name': 'number_of_replicas'``)
   * Number of replicas to be created in the second datacenter (``'datacenter_2_name': 'number_of_replicas'``)

   .. code-block:: bash

      CREATE KEYSPACE keyspace_name WITH replication =    /
      {                                                   /
        'class': 'NetworkTopologyStrategy',               /
        'datacenter_1_name': 'number_of_replicas',        /
        'datacaenter_2_name': 'number_of_replicas'        /
      }                                                   /
      AND durable_writes = true;

   .. code-block:: bash
      :caption: Example

      CREATE KEYSPACE default WITH replication =           /
      {                                                    /
        'class': 'NetworkTopologyStrategy',                /
        'dc_1': '3',                                       /
        'dc_2': '3'                                        /
      }                                                    /
      AND durable_writes = true;

.. topic:: Result

    You've set up the replication factor for your keyspace. Now all data within this keyspace gets replicated to the datacenters according to the specified factor.

.. seealso::

    For more details on the replication factor for Apache Cassandra, see `NetworkTopologyStrategy <https://cassandra.apache.org/doc/4.1/cassandra/cql/ddl.html#networktopologystrategy>`_ in the Apache Cassandra documentation.

Set up the consistency level
----------------------------

For Apache Cassandra, you can set up the ``CONSISTENCY`` parameter, which regulates when the client can concern an operation as successfully completed. The ``CONSISTENCY`` parameter defines how many nodes need to confirm the operation as finalized before the client can acknowledge the operation as successfully completed.

.. note::
    
    You can configure the consistency level in the shell or in a client library. While using the ``cqlsh`` CLI client is convenient for setting up keyspaces or testing, using a client software is recommended for operations in the production environment and bulk actions, such as data imports, data querying, or data reads/ writes from/ to databases.

In the shell
''''''''''''

.. note::
    
    This instruction uses the ``cqlsh`` Cassandra CLI client to configure the consistency level.

1. :doc:`Connect to your service via cqlsh </docs/products/cassandra/howto/connect-cqlsh-cli>`.
2. Run ``CONSISTENCY;`` to check your current setting for the consistency level.

.. topic:: Expected output

    The query can return, for example, ``Current consistency level is ONE.``, which means that a conformation of an operation completion on one node is enough for this operation to be considered as successfully completed for your service.

3. To set up the consistency level to a specific value, run the ``CONSISTENCY consistency_level_argument;`` query.

.. topic:: Allowed consistency level arguments

    * ANY
    * ONE
    * TWO
    * THREE
    * QUORUM
    * ALL
    * LOCAL_QUORUM
    * LOCAL_ONE
    * SERIAL
    * LOCAL_SERIAL

.. code-block:: bash
   :caption: Example

   CONSISTENCY QUORUM;

In a client library
'''''''''''''''''''

To configure the consistency level in a client library, add an extra parameter defining the consistency level on your object before running a particular query.

.. topic:: Result

    You've set up the consistency level for your service. Now operations on your data are considered as successfully completed according to the consistency level you specified.

.. seealso::

    For more details on consistency levels for Apache Cassandra, see `CONSISTENCY <https://cassandra.apache.org/doc/4.1/cassandra/tools/cqlsh.html#consistency>`_ in the Apache Cassandra documentation.

Related reading
---------------

* :doc:`OpenSearch® cross-cluster replication</docs/products/opensearch/concepts/cross-cluster-replication-opensearch>`
* :doc:`Set up cross-cluster replication for OpenSearch</docs/products/opensearch/howto/setup-cross-cluster-replication-opensearch>`
* :doc:`Enabling cross-cluster replication for Apache Kafka® via Terraform</docs/tools/terraform/reference/cookbook/kafka-mirrormaker-recipe>`
* `Cassandra® documentation <https://cassandra.apache.org/doc/latest/>`_
