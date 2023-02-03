Enable cross-cluster replication in Aiven for Apache Cassandra® |beta|
======================================================================

Enabling the cross-cluster replication (CCR) feature requires building a CCR setup on the Aiven side and, next, configuring the replication on the Apache Cassandra side. This article covers the first part only by providing instructions on how to set up the CCR in your Aiven for Apache Cassandra® service on the Aiven side.

For the other part - the configuration of the replication factor, which ultimately makes the replication work - see the instruction in **Set up the replication factor**.

About enabling CCR
------------------

You can enable CCR either when creating a new Aiven for Apache Cassandra service or on an existing service.

.. note::

   Enabling CCR on an existing service can affect your productions workload since CCR imposes restrictions on replication settings of the user's keyspace. Make sure you understand the impact before you enable CCR on your service.

To enable CCR, you can use the following tools:

* `Aiven console <https://console.aiven.io/>`_
* CLI
* API

Prerequisites
-------------

* Aiven account
* Depending on the method you choose to use for enabling CCR

  * Access to the `Aiven console <https://console.aiven.io/>`_
  * `cURL` CLI tool
  * `Aiven CLI tool <https://github.com/aiven/aiven-client>`_

* Aiven for Cassandra service (only if enabling CCR from an existing service)

Enable CCR in the console
-------------------------

On a new service
''''''''''''''''

1. Log in to the `Aiven console <https://console.aiven.io/>`_.
2. From the **Current services** view, select **+Create service**.
3. In the **Create service** view

   1. Select Apache Cassandra® and, next, a cloud provider and a cloud region for your service.
   2. To activate CCR, select the **Enable Cross Cluster Replication** toggle, which unfolds an additional section for setting up another Apache Cassandra service.
   3. Select a cloud provider and a cloud region for the second service.
   4. Select one service plan for your two new services.
   5. Optionally, add an additional disk storage for your services.
   6. Enter names for your services.

.. topic:: Datacenters names

   Notice that the service names you enter are automatically copied as the names for datacenters for the services. The datacenters names can be required when executing statements on your databases.

4. Verify your choices in the **Services summary** card on the right and, if your configuration turns out as expected, select **+Create services** if the setting looks.

.. topic:: Result
   
   You've created two new services that are connected for CCR purposes. You can preview CCR details for your services in the **Overview** tab under **Cross Cluster replication**.

On an existing service
''''''''''''''''''''''

1. Log in to the `Aiven console <https://console.aiven.io/>`_.
2. From the **Current services** view, select an Aiven for Apache Cassandra service on which you'd like to enable CCR.
3. In the **Overview** tab of your service's page, navigate to **Cross Cluster Replication** and select **Migrate to Cross Cluster**.

   .. note::
      
      When you enable CCR on a particular service, you create another service with the same plan, number of nodes, and disk storage.

4. In the **Create a Cross Cluster Replica** view
   
   1. Select a cloud provider and a cloud region, define a name for your new service, and select **Continue**.
   2. Examine the **Service Summary** section and make sure the configuration for your new service meets your expectations. If so, select **Create Cross Cluster Replica**. 

.. topic:: Result
   
   CCR has been enabled by connecting your service to another new service, which is now visible in the **Overview** tab under **Cross Cluster replication**.

Enable CCR with CLI
-------------------

You can enable CCR for your new or existing Aiven for Apache Cassandra service using the Aiven CLI.

.. tip::

   Check out how to get started with the Aiven CLI in :doc:`Aiven CLI </docs/tools/cli>`.

Before you start
''''''''''''''''

Understand parameters to be supplied:

* ``service_to_join_with`` parameter value needs to be set to a name of an existing service in the same project. The supplied service name indicates the service you connect to for enabling CCR. The two connected services create a CCR service pair.
* ``cassandra.datacenter`` parameter value needs to be set to a name of a datacenter for your service. Make sure each of the two service constituting a CCR pair belongs to a different datacenter.

On a new service
''''''''''''''''

Use the :ref:`avn service create <avn-cli-service-create>` command to create a new service. Add the ``service_to_join_with`` and ``cassandra.datacenter`` parameters and set their values as needed.

.. code-block:: bash

   avn service create                                   \
      --service-type cassandra                          \
      --cloud cloud_region_name                         \
      --plan service_plan_name                          \
      -c cassandra.datacenter=datacenter_name           \
      -c service_to_join_with=existing_service_name     \
      service_name

On an existing service
''''''''''''''''''''''

Use the :ref:`avn service update <avn-cli-service-update>` command to modify your service configuration by adding the ``service_to_join_with`` parameter and set its value as needed.

.. important::

   Make sure that your primary service and the service you connect to (``service_to_join_with``) are hosted on different datacenters.

.. code-block:: bash

   avn service update service_name                     \
      -c service_to_join_with=existing_service_name

Enable CCR with API
-------------------

You can enable CCR for your new or existing Aiven for Apache Cassandra service using Aiven APIs.

.. note::
   
   In this instruction, the `curl` command line tool is used to interact with Aiven APIs.

.. tip::

   Check out how to get started with Aiven APIs in :doc:`Aiven API </docs/tools/api>`.

Before you start
''''''''''''''''

Understand parameters to be supplied:

* ``service_to_join_with`` parameter value needs to be set to a name of an existing service in the same project. The supplied service name indicates the service you connect to for enabling CCR. The two connected services create a CCR service pair.
* ``cassandra.datacenter`` parameter value needs to be set to a name of a datacenter for your service. Make sure each of the two service constituting a CCR pair belongs to a different datacenter.

On a new service
''''''''''''''''

Use the `ServiceCreate <https://api.aiven.io/doc/#tag/Service/operation/ServiceCreate>`_ API to create a new service with CCR enabled. When constructing the API request, add the ``user_config`` object to the request body and nest inside it the ``service_to_join_with`` and ``datacenter`` fields.

.. code-block:: bash

   curl --request POST                                                   \
      --url https://api.aiven.io/v1/project/YOUR_PROJECT_NAME/service    \
      --header 'Authorization: Bearer YOUR_BEARER_TOKEN'                 \
      --header 'content-type: application/json'                          \
      --data
         '{
            "cloud": "string",
            "plan": "string",
            "service_name": "new_service_name",
            "service_type": "cassandra",
            "user_config": {
               "cassandra": {
                  "datacenter": "datacenter_name"
               },
               "service_to_join_with": "service_name"
            }
         }'

On an existing service
''''''''''''''''''''''

Use the `ServiceUpdate <https://api.aiven.io/doc/#tag/Service/operation/ServiceUpdate>`_ API to modify the configuration of your existing service so that it has CCR enabled. When constructing the API request, add the ``user_config`` object to the request body and nest the ``service_to_join_with`` field inside it.

.. important::

   Make sure that your primary service and the service you connect to (``service_to_join_with``) are hosted on different datacenters.

.. code-block:: bash

   curl --request PUT                                                                     \
      --url https://api.aiven.io/v1/project/YOUR_PROJECT_NAME/service/YOUR_SERVICE_NAME   \
      --header 'Authorization: Bearer YOUR_BEARER_TOKEN'                                  \
      --header 'content-type: application/json'                                           \
      --data                                                                              \
         '{
            "user_config": {
               "service_to_join_with":"service_name"
            }
         }'

Related reading
---------------

* :doc:`OpenSearch® cross-cluster replication</docs/products/opensearch/concepts/cross-cluster-replication-opensearch>`
* :doc:`Set up cross-cluster replication for OpenSearch</docs/products/opensearch/howto/setup-cross-cluster-replication-opensearch>`
* :doc:`Enabling cross-cluster replication for Apache Kafka® via Terraform</docs/tools/terraform/reference/cookbook/kafka-mirrormaker-recipe>`
* `Multi-master Replication: Versioned Data and Tunable Consistency <https://cassandra.apache.org/doc/latest/cassandra/architecture/dynamo.html#multi-master-replication-versioned-data-and-tunable-consistency>`_
