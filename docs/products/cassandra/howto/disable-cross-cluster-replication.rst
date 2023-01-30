Disable cross-cluster replication in Aiven for Apache Cassandra® |private beta|
===============================================================================

.. important::

   This private beta feature is available on request only. Contact sales@Aiven.io or support@Aiven.io to opt in. 

This article provides you with instructions on how to discontinue the cross-cluster replication (CCR) for your Aiven for Apache Cassandra® service.

About disabling CCR
-------------------

When you enable CCR for your service, you connect it to another service (replica service), which results in creating a CCR pair of services. You can disable CCR for your service either by splitting the services constituting the CCR pair or by deleting one of them.

* `Aiven console <https://console.aiven.io/>`_
* CLI
* API

It's recommended to use the Aiven console for disabling CCR.

Prerequisites
-------------

* Aiven account
* Depending on the method you choose to use for enabling CCR

  * Access to the `Aiven console <https://console.aiven.io/>`_
  * `cURL` CLI tool
  * `Aiven CLI tool <https://github.com/aiven/aiven-client>`_

* CCR enabled on a pair of Aiven for Apache Cassandra services

Disable CCR in the console
--------------------------

In the console, use either of the two following methods to disable CCR on your service(s): split the services or delete one of them.

Split the services
''''''''''''''''''

1. Log in to the `Aiven console <https://console.aiven.io/>`_.
2. From the **Current services** view, select the service for which you'd like to disable CCR.
3. In the **Overview** tab of the service's page, navigate to **Cross Cluster Replication** and select **Split cluster**.

   .. warning::

      As soon as you split the cluster, the two services constituting the CCR pair become independent. It's not possible to recreate the CCR pair with the same service as a replica. You can select any other Aiven for Cassandra service for that purpose.
   
4. When in the **Warning** popup, make sure you understand the impact and select **Split cluster**.

.. topic:: Result

   You service no longer has a cross-cluster replica.

Delete a service
''''''''''''''''

To disable CCR on your service, delete the replica service that is connected to your services for CCR purposes.

1. Log in to the `Aiven console <https://console.aiven.io/>`_.
2. From the **Current services** view, select an Aiven for Apache Cassandra service on which you'd like to enable CCR.
3. In the **Overview** tab of the service's page, navigate to the **Cross Cluster Replication** section and select the name of the replica service provided in the CCR description, which is supposed to take you to the replica service's page.
4. In the **Overview** tab of the replica service, select **Delete service** from the top right corner.

   .. warning::

      As soon as you delete the replica service, CCR gets disabled for your service that is now connected to the replica service for CCR purposes.

5. When in the **Delete confirmation** popup, make sure you understand the impact, copy-paste the service name, and select **Delete**.

.. topic:: Result

   You've disable CCR on your service, which no longer has a cross-cluster replica since the replica service has been deleted.

Disable CCR with CLI
--------------------

You can disable CCR for your Aiven for Apache Cassandra service using the Aiven CLI to delete one of the services constituting the CCR pair.

.. tip::

   Check out how to get started with the Aiven CLI in :doc:`Aiven CLI </docs/tools/cli>`.

Use the :ref:`avn service terminate <avn-cli-service-terminate>` command to disable CCR on your service by deleting its replica service.

.. code-block:: bash

   avn service terminate replica_service_name

Disable CCR with API
--------------------

You can disable CCR for your Aiven for Apache Cassandra service(s) by calling the `terminate a service <https://api.aiven.io/doc/#tag/Service/operation/ServiceDelete>`_ endpoint to delete one of the services that constitute the CCR pair.

.. note::
   
   In this instruction, the `curl` command line tool is used to interact with Aiven APIs.

.. tip::

   Check out how to get started with Aiven APIs in :doc:`Aiven API </docs/tools/api>`.

To call the `terminate a service <https://api.aiven.io/doc/#tag/Service/operation/ServiceDelete>`_ endpoint, specify the project name and the service name as path parameters and provide your token as a header in the request.

.. code-block:: bash

   curl --request DELETE \
      --url https://api.aiven.io/v1/project/PROJECT_NAME/service/SERVICE_NAME \
      --header 'Authorization: Bearer YOUR_TOKEN'

Related reading
---------------

* :doc:`OpenSearch® cross-cluster replication</docs/products/opensearch/concepts/cross-cluster-replication-opensearch>`
* :doc:`Set up cross-cluster replication for OpenSearch</docs/products/opensearch/howto/setup-cross-cluster-replication-opensearch>`
* :doc:`Enabling cross-cluster replication for Apache Kafka® via Terraform</docs/tools/terraform/reference/cookbook/kafka-mirrormaker-recipe>`
* `Cassandra® documentation <https://cassandra.apache.org/doc/latest/>`_
