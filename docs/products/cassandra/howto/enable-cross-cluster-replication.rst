Enable cross-cluster replication in Aiven for Apache Cassandra® |beta|
======================================================================

Enabling the cross-cluster replication (CCR) feature requires building a CCR setup in the Aiven platform and, next, configuring the replication on the Apache Cassandra side. This article covers the first part only by providing instructions on how to set up CCR for your Aiven for Apache Cassandra® service on the Aiven side.

For the other part (the configuration of the replication factor on the Apache Cassandra side), which ultimately makes the replication work, see the instruction in :ref:`Set up the replication factor <set-up-replication-factor>`.

About enabling CCR
------------------

You can enable CCR either when creating a new Aiven for Apache Cassandra service or for an existing service.

Limitations
'''''''''''

See :ref:`CCR limitations <ccr-limitations>` for limitations that apply to CCR on Aiven for Apache Cassandra.

Tools
'''''

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

* See :ref:`Limitations <ccr-limitations>`.

Enable CCR in the console
-------------------------

Using the `Aiven web console <https://console.aiven.io/>`_, you can enable CCR for

* New Aiven for Apache Cassandra service by :ref:`creating a totally new CCR service pair <new-pair>` or
* Existing Aiven for Apache Cassandra service by :ref:`adding a CCR peer service in another region to an existing service <new-peer>`.

.. _new-pair:

Create a new CCR service pair
'''''''''''''''''''''''''''''

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

.. _new-peer:

Add a CCR peer to an existing service
'''''''''''''''''''''''''''''''''''''

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

Using CLI, you can enable CCR for

* New Aiven for Apache Cassandra service by :ref:`creating a totally new CCR service pair <new-ccr-service-pair>` or
* Existing Aiven for Apache Cassandra service by :ref:`adding a CCR peer service in another region to an existing service <new-ccr-peer-service>`.

.. note::
   
   In this instruction, the :doc:`Aiven CLI client </docs/tools/cli>` is used to interact with Aiven APIs.

.. topic:: Understand parameters to be supplied

   * ``service_to_join_with`` parameter value needs to be set to a name of an existing service in the same project. The supplied service name indicates the service you connect to for enabling CCR. The two connected services create a CCR service pair.
   * ``cassandra.datacenter`` is a datacenter name used to identify nodes from a particular service in the cluster's topology. In CCR for Aiven for Apache Cassandra, all nodes of either of the two services belong to a single datacenter; therefore, a value of the ``cassandra.datacenter`` parameter needs to be unique for each service. It's recommended to set it equal to the service name.

.. _new-ccr-service-pair:

Create a new CCR service pair
'''''''''''''''''''''''''''''

1. Use the :ref:`avn service create <avn-cli-service-create>` command to create a new service (``service_1``).

   .. code-block:: bash

      avn service create                                   \
         --service-type cassandra                          \
         --cloud cloud_region_name                         \
         --plan service_plan_name                          \
         -c cassandra.datacenter=datacenter_1_name         \
         service_1_name

2. Create another new service (``service_2``). This time, include the ``service_to_join_with`` parameter to connect it to ``service_1`` and create a CCR pair. Set the value of the ``service_to_join_with`` parameter to the name of ``service_1``.

   .. important::

      See :ref:`Limitations <limitations>` before you set the parameters.

   .. code-block:: bash

      avn service create                                   \
         --service-type cassandra                          \
         --cloud cloud_region_name                         \
         --plan service_plan_name                          \
         -c cassandra.datacenter=datacenter_2_name         \
         -c service_to_join_with=service_1_name            \
         service_2_name

.. _new-ccr-peer-service:

Add a CCR peer to an existing service
'''''''''''''''''''''''''''''''''''''

Use the :ref:`avn service create <avn-cli-service-create>` command to create a new service with CCR enabled. Use the ``service_to_join_with`` parameter to connect your new service to an existing service creating a CCR pair. Set the value of the ``service_to_join_with`` parameter to the name of the existing service.

.. important::

   See :ref:`Limitations <limitations>` before you set the parameters.

.. code-block:: bash

   avn service create                                   \
      --service-type cassandra                          \
      --cloud cloud_region_name                         \
      --plan service_plan_name                          \
      -c cassandra.datacenter=datacenter_name           \
      -c service_to_join_with=existing_service_name     \
      new_service_name

Enable CCR with API
-------------------

Using :doc:`Aiven APIs </docs/tools/api>`, you can enable CCR for

* New Aiven for Apache Cassandra service by :ref:`creating a totally new CCR service pair <new-ccr-pair>` or
* Existing Aiven for Apache Cassandra service by :ref:`adding a CCR peer service in another region to an existing service <new-ccr-peer>`.

.. note::
   
   In this instruction, the `curl` command line tool is used to interact with Aiven APIs.

.. topic:: Understand parameters to be supplied

   * ``service_to_join_with`` parameter value needs to be set to a name of an existing service in the same project. The supplied service name indicates the service you connect to for enabling CCR. The two connected services create a CCR service pair.
   * ``cassandra.datacenter`` is a datacenter name used to identify nodes from a particular service in the cluster's topology. In CCR for Aiven for Apache Cassandra, all nodes of either of the two services belong to a single datacenter; therefore, a value of the ``cassandra.datacenter`` parameter needs to be unique for each service. It's recommended to set it equal to the service name.

.. _new-ccr-pair:

Create a new CCR service pair
'''''''''''''''''''''''''''''

Use the `ServiceCreate <https://api.aiven.io/doc/#tag/Service/operation/ServiceCreate>`_ API to create a new service with CCR enabled. When constructing the API request, add the ``user_config`` object to the request body and nest inside it the ``service_to_join_with`` and ``datacenter`` fields.

1. Use the `ServiceCreate <https://api.aiven.io/doc/#tag/Service/operation/ServiceCreate>`_ API to create a new service (``service_1``).

   .. code-block:: bash

      curl --request POST                                                   \
         --url https://api.aiven.io/v1/project/YOUR_PROJECT_NAME/service    \
         --header 'Authorization: Bearer YOUR_BEARER_TOKEN'                 \
         --header 'content-type: application/json'                          \
         --data
            '{
               "cloud": "string",
               "plan": "string",
               "service_name": "service_1_name",
               "service_type": "cassandra"
            }'

2. Create another new service (``service_2``). This time when constructing the API request, add the ``user_config`` object to the request body and nest inside it the ``service_to_join_with`` and ``datacenter`` fields. Set the value of the ``service_to_join_with`` parameter to the name of ``service_1`` to connect both services and create a CCR pair.

   .. important::

      See :ref:`Limitations <limitations>` before you set the parameters.

   .. code-block:: bash

      curl --request POST                                                   \
         --url https://api.aiven.io/v1/project/YOUR_PROJECT_NAME/service    \
         --header 'Authorization: Bearer YOUR_BEARER_TOKEN'                 \
         --header 'content-type: application/json'                          \
         --data
            '{
               "cloud": "string",
               "plan": "string",
               "service_name": "service_2_name",
               "service_type": "cassandra",
               "user_config": {
                  "cassandra": {
                     "datacenter": "datacenter_name"
                  },
                  "service_to_join_with": "service_1_name"
               }
            }'

.. _new-ccr-peer:

Add a CCR peer to an existing service
'''''''''''''''''''''''''''''''''''''

Use the `ServiceCreate <https://api.aiven.io/doc/#tag/Service/operation/ServiceCreate>`_ API to create a new service with CCR enabled. When constructing the API request, add the ``user_config`` object to the request body and nest inside it the ``service_to_join_with`` and ``datacenter`` fields. Set the value of the ``service_to_join_with`` parameter to the name of your existing service to connect it to your new service and create a CCR pair.

.. important::

   See :ref:`Limitations <limitations>` before you set the parameters.

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
                  "service_to_join_with": "existing_service_name"
               }
            }'

What's next
-----------

* :doc:`Manage CCR on Aiven for Apache Cassandra </docs/products/cassandra/howto/manage-cross-cluster-replication>`
* :doc:`Disable CCR on Aiven for Apache Cassandra </docs/products/cassandra/howto/disable-cross-cluster-replication>`

Related reading
---------------

* :doc:`About cross-cluster replication on Aiven for Apache Cassandra </docs/products/cassandra/concepts/cross-cluster-replication>`
* `Multi-master Replication: Versioned Data and Tunable Consistency <https://cassandra.apache.org/doc/latest/cassandra/architecture/dynamo.html#multi-master-replication-versioned-data-and-tunable-consistency>`_
* :doc:`OpenSearch® cross-cluster replication</docs/products/opensearch/concepts/cross-cluster-replication-opensearch>`
* :doc:`Set up cross-cluster replication for OpenSearch</docs/products/opensearch/howto/setup-cross-cluster-replication-opensearch>`
* :doc:`Enabling cross-cluster replication for Apache Kafka® via Terraform</docs/tools/terraform/reference/cookbook/kafka-mirrormaker-recipe>`
