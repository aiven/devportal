Disable cross-cluster replication in Aiven for Apache Cassandra®
================================================================

.. important::

    Aiven for Apache Cassandra® cross-cluster replication (CCR) is a limited availability feature. If you're interested in trying out this feature, contact the sales team at `sales@Aiven.io <mailto:sales@Aiven.io>`_.

This article provides you with instructions on how to discontinue the cross-cluster replication (CCR) for your Aiven for Apache Cassandra® service.

About disabling CCR
-------------------

When you enable CCR for your service, you connect it to another service, which results in creating a CCR pair of services. You can disable CCR for your service either by splitting the services constituting the CCR pair or by deleting one of them.

* `Aiven Console <https://console.aiven.io/>`_
* CLI
* API

It's recommended to use Aiven Console for disabling CCR.

.. warning::

   As soon as you split the cluster, the two services constituting the CCR pair become independent. It's not possible to recreate the CCR pair connecting back to the same service. To enable CCR on your service again, you can create a new service and CCR-connect it to your existing service.

Prerequisites
-------------

* Aiven account
* Depending on the method you choose to use for disabling CCR

  * Access to `Aiven Console <https://console.aiven.io/>`_
  * `cURL` CLI tool
  * `Aiven CLI tool <https://github.com/aiven/aiven-client>`_

* CCR enabled on a pair of Aiven for Apache Cassandra services

Disable CCR in the console
--------------------------

In the console, use either of the two following methods to disable CCR on your service(s): split the services or delete one of them.

Split the services
''''''''''''''''''

1. Log in to `Aiven Console <https://console.aiven.io/>`_.
2. From the **Services** page, select the service for which you'd like to disable CCR.
3. In the **Overview** page of the service, navigate to **Cross Cluster Replication** and select **Split cluster**.
4. In the **Warning** popup, get familiar with the consequences of splitting the cluster, make sure you understand the impact, and select **Split cluster**.

.. topic:: Result

   You service no longer replicates to the other service since the services have been disconnected.

Delete a service
''''''''''''''''

To disable CCR on your service, delete the service that is connected to your services for CCR purposes.

1. Log in to `Aiven Console <https://console.aiven.io/>`_.
2. From the **Services** page, select an Aiven for Apache Cassandra service on which you'd like to enable CCR.
3. In the **Overview** page of the service, navigate to the **Cross Cluster Replication** section and select the name of the service provided in the CCR description, which is supposed to take you to the service's page.
4. In the **Overview** page of the service, select **Delete service** from the meatballs menu in the top right corner.

   .. warning::

      As soon as you delete the service where your data has been replicated, CCR gets disabled and your data is no longer replicated between regions.

5. When in the **Delete confirmation** popup, make sure you understand the impact, copy-paste the service name, and select **Delete**.

.. topic:: Result

   You've disabled CCR on your service by deleting one of the peer services in the CCR service pair.

Disable CCR with CLI
--------------------

You can disable CCR for your Aiven for Apache Cassandra service using the Aiven CLI to delete one of the services constituting the CCR pair.

.. tip::

   Check out how to get started with the Aiven CLI in :doc:`Aiven CLI </docs/tools/cli>`.

Use the :ref:`avn service terminate <avn-cli-service-terminate>` command to disable CCR on your service by deleting the service used as a sink for your replicated data.

.. code-block:: bash

   avn service terminate ccr_peer_service_name

Disable CCR with API
--------------------

You can disable CCR for your Aiven for Apache Cassandra service(s) by calling the `ServiceDelete <https://api.aiven.io/doc/#tag/Service/operation/ServiceDelete>`_ endpoint to delete one of the services that constitute the CCR pair.

.. note::
   
   In this instruction, the `curl` command line tool is used to interact with Aiven APIs.

.. tip::

   Check out how to get started with Aiven APIs in :doc:`Aiven API </docs/tools/api>`.

To call the `ServiceDelete <https://api.aiven.io/doc/#tag/Service/operation/ServiceDelete>`_ endpoint, specify the project name and the service name as path parameters and provide your token as a header in the request.

.. code-block:: bash

   curl --request DELETE \
      --url https://api.aiven.io/v1/project/PROJECT_NAME/service/SERVICE_NAME \
      --header 'Authorization: Bearer YOUR_TOKEN'

More on Apache Cassandra CCR
----------------------------

* :doc:`About cross-cluster replication on Aiven for Apache Cassandra </docs/products/cassandra/concepts/cross-cluster-replication>`
* :doc:`Enable CCR on Aiven for Apache Cassandra </docs/products/cassandra/howto/enable-cross-cluster-replication>`
* :doc:`Manage CCR on Aiven for Apache Cassandra </docs/products/cassandra/howto/manage-cross-cluster-replication>`

More on CCR with Aiven
----------------------

* :doc:`OpenSearch® cross-cluster replication</docs/products/opensearch/concepts/cross-cluster-replication-opensearch>`
* :doc:`Set up cross-cluster replication for OpenSearch</docs/products/opensearch/howto/setup-cross-cluster-replication-opensearch>`
* :doc:`Enabling cross-cluster replication for Apache Kafka® via Terraform</docs/tools/terraform/reference/cookbook/kafka-mirrormaker-recipe>`
