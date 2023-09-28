Use Azure Private Link with Aiven services 
===========================================

.. important::

    Azure Private Link is a :doc:`limited availability feature </docs/platform/concepts/beta_services>`, which you can request from the sales team (sales@Aiven.io) or your account manager. During the limited availability stage, you can use the feature at no cost. If you want to continue using Azure Private Link after it reaches general availability, you'll be billed according to the latest applicable price.

Azure Private Link lets you bring your Aiven services into your virtual network (VNet) over a private endpoint. The endpoint creates a network interface into one of the VNet subnets, and receives a private IP address from its IP range. The private endpoint is routed to your Aiven service.

Azure Private Link is supported for the following services:

* Aiven for Apache Kafka®
* Aiven for Apache Kafka Connect®
* Aiven for ClickHouse®
* Aiven for Grafana®
* Aiven for InfluxDB®
* Aiven for MySQL®
* Aiven for OpenSearch®
* Aiven for PostgreSQL®
* Aiven for Redis®*

Prerequisites
--------------

* :doc:`Aiven CLI </docs/tools/cli>` is installed.
* The Aiven service is in :doc:`a project VPC </docs/platform/howto/manage-vpc-peering>`. This ensures the service is not accessible from the public internet. 
  
  .. Note::
  
    If you are not using regular VNet peerings, any private IP range can be used for the VPC. There is no network routing between your Azure subscription and the Aiven VPC, so overlapping IP ranges are not an issue.

* The Aiven service is using :doc:`static IP addresses </docs/platform/howto/static-ip-addresses>`.

  .. Note::
  
    Even though services in a VPC only communicate using private IP addresses, Azure load balancers require `standard SKU IP addresses <https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/public-ip-upgrade-portal>`_ for target virtual machines. Azure sends TCP health probes to load balancer target ports from a public IP address.

Variables
------------

.. list-table::
    :header-rows: 1
    :align: left

    * - Variable
      - Description

    * - ``SUBSCRIPTION_ID``
      - Azure subscription ID
    * - ``AIVEN_SERVICE``
      - Name of your Aiven service

Set up a Private Link connection
----------------------------------
There are three steps to setting up an Azure Private Link with your Aiven service:

1. Create a Private Link service
2. Create a private endpoint
3. Enable Private Link access service components

Step 1: Create a Private Link service
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. In the Aiven CLI, create a Private Link resource on your Aiven service:

   .. code:: shell

      avn service privatelink azure create AIVEN_SERVICE --user-subscription-id SUBSCRIPTION_ID

   This creates an `Azure Standard Internal Load Balancer <https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-overview>`_ dedicated to your Aiven service and attaches it to an Azure Private Link service. Connections from other subscriptions are automatically rejected.

#. Check the status of the Private Link service:

   .. code:: shell

    avn service privatelink azure get AIVEN_SERVICE

   The service is in the ``creating`` state until Azure provisions a load balancer and Private Link service.

#. When the state changes to ``active``, note the ``azure_service_alias`` and ``azure_service_id``:

   .. code:: shell

    avn service privatelink azure get AIVEN_SERVICE

Step 2: Create a private endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Azure resources in the Aiven service are now ready to be connected to your Azure subscription and virtual network.

#. In the Azure web console or Azure CLI, `create a private endpoint <https://learn.microsoft.com/en-us/azure/private-link/create-private-endpoint-portal?tabs=dynamic-ip>`_. If you are using the console, select **Connect to an Azure resource by resource ID or alias** and enter the ``azure_service_alias`` or ``azure_service_id``.

#. Refresh the Aiven Private Link service:

   .. code:: shell

    avn service privatelink azure refresh AIVEN_SERVICE

   .. Note::
   
    Azure does not provide notifications about endpoint connections and the Aiven API will not be aware of new endpoints until it's refreshed.

#. In the Aiven CLI, check that the endpoint is connected to the service:

   .. code:: shell

    avn service privatelink azure connection list AIVEN_SERVICE

   The output will look similar to this:

   .. code:: shell

       PRIVATELINK_CONNECTION_ID  PRIVATE_ENDPOINT_ID                                                                                                                                         STATE                  USER_IP_ADDRESS
       =========================  ==========================================================================================================================================================  =====================  ===============
       plc35843e8054b             /subscriptions/8eefec94-5d63-40c9-983c-03ab083b411d/resourceGroups/test-privatelink/providers/Microsoft.Network/privateEndpoints/my-endpoint                pending-user-approval  null

#. Check that the endpoint ID matches the one created in your subscription and approve it:

   .. code:: shell

    avn service privatelink azure connection approve AIVEN_SERVICE PRIVATELINK_CONNECTION_ID

   The endpoint in your Azure subscription is now connected to the Private Link service in the Aiven service. The state of the endpoint is ``pending``.

#. In the Azure web console, go to the private endpoint and select **Network interface**. Copy the private IP address.

#. In the Aiven CLI, add the endpoint's IP address you copied to the connection:

   .. code:: shell

     avn service privatelink azure connection update \
        --endpoint-ip-address IP_ADDRESS             \
        AIVEN_SERVICE PRIVATELINK_CONNECTION_ID

Once the endpoint IP address is added, the connection's status changes to ``active``. A DNS name for the service is registered pointing to that IP address.

Step 3: Enable Private Link access for Aiven service components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Finally, enable Private Link access on your Aiven services using either the Aiven CLI or `Aiven Console <https://console.aiven.io/>`_.

**Aiven CLI**

To enable Private Link access for your service in the Aiven CLI, set ``user_config.privatelink_access.<service component>`` to true for the components you want to enable. For example, for PostgreSQL the command is:

.. code:: shell

    avn service update -c privatelink_access.pg=true AIVEN_SERVICE

**Aiven Console**

To enable Private Link access in `Aiven Console <https://console.aiven.io/>`_:

#. Select the service that you want to enable access to.
#. On the **Overview** page of your service, in the **Advanced configuration** section, select **Change**.
#. Select **Add configuration option** > ``privatelink_access.<service component>`` for the components that you want to enable.
#. Toggle the switch next to the components to set the values to true.
#. Select **Save advanced configuration**.

.. Tip::

    Each service component can be controlled separately. For example, you can enable Private Link access for your Aiven for Apache Kafka® service, while allowing Kafka® Connect to only be connected via VNet peering.

After toggling the values, your Private Link resource will be rebuilt with load balancer rules added for the service component's ports.

.. note::
  
  For Aiven for Apache Kafka® services, the security group for the VPC endpoint must allow ingress in the port range ``10000-31000``. This is to accommodate the pool of Kafka broker ports used in the Private Link implementation.

Acquire connection information
------------------------------

.. _one-privatelink-connection:

One Azure Private Link connection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have Azure Private Link enabled for one service component, you can preview its connection information (URI, hostname, or port required to access the service through the private endpoint) on the service's **Overview** page in `Aiven Console <https://console.aiven.io/>`_.

Multiple Azure Private Link connections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have more than one Azure Private Link connection, you can get connection information for the first connection as described in :ref:`One Azure Private Link connection <one-privatelink-connectio>` from `Aiven Console <https://console.aiven.io>`__. For connection information on the remaining connections, you need to use CLI.

Each endpoint (connection) has PRIVATELINK_CONNECTION_ID, which you can check using the ``avn service privatelink azure connection list SERVICE_NAME`` command.

* To acquire SSL connection information for your service using Azure Private Link, run the following command:

.. code-block:: bash

   avn service connection-info UTILITY_NAME SERVICE_NAME -p PRIVATELINK_CONNECTION_ID

.. topic:: Where

  * UTILITY_NAME is ``kcat``, for example
  * SERVICE_NAME is ``kafka-12a3b4c5``, for example
  * PRIVATELINK_CONNECTION_ID is ``plc39413abcdef``, for example

* To acquire connection information for your service using Azure Private Link with SASL enabled, run the following command:

.. code-block:: bash

   avn service connection-info UTILITY_NAME SERVICE_NAME -p PRIVATELINK_CONNECTION_ID -a sasl

.. topic:: Where

  * UTILITY_NAME is ``kcat``, for example
  * SERVICE_NAME is ``kafka-12a3b4c5``, for example
  * PRIVATELINK_CONNECTION_ID is ``plc39413abcdef``, for example

.. note::

   SSL certificates and SASL credentials are the same for all the connections.

Update subscription list
------------------------
In the Aiven CLI, you can update the list of Azure subscriptions that have access to Aiven service endpoints:

.. code:: shell

    avn service privatelink azure update AIVEN_SERVICE SUBSCRIPTION_ID

Delete a Private Link service
-----------------------------
Use the Aiven CLI to delete the Azure Load Balancer and Private Link service:

.. code:: shell

    avn service privatelink azure delete AIVEN_SERVICE
