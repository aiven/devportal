Manage cross-cluster replication in Aiven for Apache Cassandra®
===============================================================

.. important::

    Aiven for Apache Cassandra® cross-cluster replication (CCR) is a :doc:`limited availability feature </docs/platform/concepts/beta_services>`. If you're interested in trying out this feature, contact the sales team at `sales@Aiven.io <mailto:sales@Aiven.io>`_.

Learn how to update Apache Cassandra® services that has cross-cluster replication (CCR) enabled: change the service plan and add an extra disk space. Find out how to set up the replication factor and the consistency level for your CCR-enabled Apache Cassandra® services.

Prerequisites
-------------

Aiven-wise
''''''''''

* Aiven account
* Pair of Aiven for Apache Cassandra services with CCR enabled

Tools
'''''

* To update the service plan or add an extra disk space, use `Aiven Console <https://console.aiven.io/>`_.
* To set up the replication factor on the database side, issue the CREATE KEYSPACE statement from `any supported client driver <https://cassandra.apache.org/doc/latest/cassandra/getting_started/drivers.html>`_. This guide uses the ``cqlsh`` Cassandra client for that purpose to ensure general applicability of the instruction.
* To set up the consistency level on the client side, configure it in your software. This guide uses the ``cqlsh`` Cassandra client for that purpose to ensure general applicability of the instruction.

Change the service plan
-----------------------

.. important::

    When you change the plan for your CCR-enabled service, the plan for the connected replica service changes accordingly since the services constituting a CCR pair always share the same service plan.

.. note::
    
    It's recommended to use the `Aiven console <https://console.aiven.io/>`_ for changing the plan for a CCR-enabled service.

1. Log in to `Aiven Console <https://console.aiven.io/>`_.
2. From the **Services** page, select a CCR-enabled Aiven for Apache Cassandra service that you want to update.
3. In the **Overview** page of your service, navigate to **Service plan** and select **Change plan**.
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
    
    It's recommended to use `Aiven Console <https://console.aiven.io/>`_ for adding storage space for CCR-enabled services.

1. Log in to `Aiven Console <https://console.aiven.io/>`_.
2. From the **Services** page, select a CCR-enabled Aiven for Apache Cassandra service that you want to update.
3. In the **Overview** page of your service, navigate to the **Service plan** section and select **Add storage**.
4. In the **Upgrade service storage** view, use the slider to add extra disk space for your service.

   .. tip::
    
      You can also change your service plan by selecting **Change plan** in the **Your current plan** section.

.. topic:: Result
    
    You've added extra disk storage space for your CCR-enabled service and its CCR-replica service.

.. _set-up-replication-factor:

Set up the replication factor
-----------------------------

You can specify how many replicas of your data you'd like to have on either of datacenters hosting your service.
For that purpose, you need a keyspace with the ``NetworkTopologyStrategy`` replication. To create a keyspace that supports CCR and defines the replication factor, you need to run the ``CREATE KEYSPACE`` query with a set of parameters configuring the keyspace as needed.

.. note::
    
    This instruction uses the ``cqlsh`` Cassandra CLI client to configure the replication factor. ``cqlsh`` is used for demonstration purposes and the same statements can be executed using any `supported client driver <https://cassandra.apache.org/doc/latest/cassandra/getting_started/drivers.html>`_.

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

For Apache Cassandra, you can set up the ``CONSISTENCY`` parameter, which regulates when the client can consider an operation as successfully completed. The ``CONSISTENCY`` parameter defines how many nodes need to confirm the operation as finalized before the client can acknowledge the operation as successfully completed.

.. note::
    
    You can configure the consistency level in the shell or in a client library. While using the ``cqlsh`` CLI client is convenient for setting up keyspaces or testing, configuring and using a `client driver <https://cassandra.apache.org/doc/latest/cassandra/getting_started/drivers.html>`_ is recommended for operations in the production environment, such as data imports, data querying, or data reads/writes from/to databases.

In the shell
''''''''''''

.. note::
    
    This instruction uses the ``cqlsh`` Cassandra CLI client to configure the consistency level.

1. :doc:`Connect to your service via cqlsh </docs/products/cassandra/howto/connect-cqlsh-cli>`.
2. Run ``CONSISTENCY;`` to check your current setting for the consistency level.

.. topic:: Expected output

    The query can return, for example, ``Current consistency level is ONE.``, which means that a confirmation of an operation completion on one node is enough for this operation to be considered as successful.

1. To set up the consistency level to a specific value, run the ``CONSISTENCY consistency_level_argument;`` query.

.. topic:: Allowed consistency level arguments

    For the list of the allowed consistency level arguments for Apache Cassandra, see `CONSISTENCY <https://cassandra.apache.org/doc/4.1/cassandra/tools/cqlsh.html#consistency>`_ in the Apache Cassandra documentation.

.. code-block:: bash
   :caption: Example

   CONSISTENCY QUORUM;

In a client library
'''''''''''''''''''

To configure the consistency level in a client library, add an extra parameter or object to define the consistency level on your software component before running a particular query.

.. topic:: Example::
    
    In Python, you can specify `consistency_level`` as a parameter for the `SimpleStatement` object.

   .. code-block:: bash
    
      session.execute(SimpleStatement("LIST ROLES", consistency_level=ConsistencyLevel.ALL))

.. topic:: Result

    You've set up the consistency level for your service. Now operations on your data are considered as successfully completed according to the consistency level you specified.

.. seealso::

    For more details on consistency levels for Apache Cassandra, see `CONSISTENCY <https://cassandra.apache.org/doc/4.1/cassandra/tools/cqlsh.html#consistency>`_ in the Apache Cassandra documentation.

More on Apache Cassandra CCR
----------------------------

* :doc:`About cross-cluster replication on Aiven for Apache Cassandra </docs/products/cassandra/concepts/cross-cluster-replication>`
* :doc:`Enable CCR on Aiven for Apache Cassandra </docs/products/cassandra/howto/enable-cross-cluster-replication>`
* :doc:`Disable CCR on Aiven for Apache Cassandra </docs/products/cassandra/howto/disable-cross-cluster-replication>`

More on CCR with Aiven
----------------------

* :doc:`OpenSearch® cross-cluster replication</docs/products/opensearch/concepts/cross-cluster-replication-opensearch>`
* :doc:`Set up cross-cluster replication for OpenSearch</docs/products/opensearch/howto/setup-cross-cluster-replication-opensearch>`
* :doc:`Enabling cross-cluster replication for Apache Kafka® via Terraform</docs/tools/terraform/reference/cookbook/kafka-mirrormaker-recipe>`
