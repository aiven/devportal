Use Azure Private Link with Aiven services
=============================================

Azure Private Link lets you bring your Aiven services into your virtual network (VNet) over a private endpoint. The endpoint creates a network interface into one of the VNet subnets, and receives a private IP address from its IP range. The private endpoint is routed to your Aiven service.

Prerequisites
--------------

* :doc:`Aiven CLI <docs/tools/cli>`` is installed.
* The Aiven service is in :doc:`a project VPC <docs/platform/howto/manage-vpc-peering>`. This ensures the service is not accessible from the public internet. 
  
  If you are not using regular VNet peerings, any private IP range can be used for the VPC. There is no network routing between your Azure subscription and the Aiven VPC, so overlapping IP ranges are not an issue.

* The Aiven service is using :doc:`static IP addresses </docs/platform/howto/static-ip-addresses>`.

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

    avn service privatelink azure create --user-subscription-id SUBSCRIPTION_ID

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

1. In the Azure web console or Azure CLI, `create a private endpoint <https://learn.microsoft.com/en-us/azure/private-link/create-private-endpoint-portal?tabs=dynamic-ip>`_.
    * In the web console, select **Connect to an Azure resource by resource ID or alias** and enter the ``azure_service_alias`` or ``azure_service_id``.

2. Refresh the Aiven Private Link service:

.. code:: shell

    avn service privatelink azure refresh AIVEN_SERVICE

Azure does not provide notifications about endpoint connections and the Aiven API will not be aware of new endpoints until it's refreshed.

3. In the Aiven CLI, check that the endpoint is connected to the service:

.. code:: shell

    avn service privatelink azure connection list AIVEN_SERVICE

The output will look similar to this:

.. code:: shell

    PRIVATELINK_CONNECTION_ID  PRIVATE_ENDPOINT_ID                                                                                                                                         STATE                  USER_IP_ADDRESS
    =========================  ==========================================================================================================================================================  =====================  ===============
    plc35843e8054b             /subscriptions/8eefec94-5d63-40c9-983c-03ab083b411d/resourceGroups/test-privatelink/providers/Microsoft.Network/privateEndpoints/my-endpoint                pending-user-approval  null

4. Check that the endpoint ID matches the one created in your subscription and approve it:

.. code:: shell

    avn service privatelink azure connection approve AIVEN_SERVICE PRIVATELINK_CONNECTION_ID

The endpoint in your Azure subscription is now connected to the Private Link service in the Aiven service. The state of the endpoint is ``pending``.

5. In the Azure web console, go to the private endpoint and select **Network interface**. Copy the private IP address.

6. In the Aiven CLI, add the endpoint's IP address you copied to the connection:

.. code:: shell

    avn service privatelink azure connection update --endpoint-ip-address IP_ADDRESS AIVEN_SERVICE PRIVATELINK_CONNECTION_ID

Once the endpoint IP address is added, the connection's status changes to ``active``. A DNS name for the service is registered pointing to that IP address.

Step 3: Enable Private Link access for Aiven service components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Finally, enable Private Link access on your Aiven services using either the Aiven CLI or Aiven Console.

**Aiven CLI**
To enable Private Link access for your service in the Aiven CLI, set ``user_config.privatelink_access.<service component>`` to true for the components you want to enable. For example, for PostgreSQL the command is:

.. code:: shell

    avn service update -c privatelink_access.pg=true AIVEN_SERVICE

**Aiven Console**
To enable Private Link access in the Aiven Console:
#. Select the service that you want to enable access to.
#. On the **Overview** tab, in the **Advanced configuration** section, click **Change**.
#. Click **Add configuration option** and select the ``privatelink_access.<service component>`` option for the components that you want to enable.
#. Toggle the switch next to the components to set the values to true.
#. Click **Save advanced configuration**.

Each service component can be controlled separately. For example, you can enable Private Link access for your Aiven for Apache Kafka® service, while allowing Kafka® Connect to only be connected via VNet peering.

After toggling the values your Private Link resource will be rebuilt with load balancer rules added for the service component's ports.Connection information like the URI or hostname and port to access the service through the private endpoint is available on the service's overview page in the Aiven Console. 

.. note:: For Aiven for Apache Kafka® services, the security group for the VPC endpoint must allow ingress in the port range ``10000-31000``. This is to accommodate the pool of Kafka broker ports used in the Private Link implementation.

Update subscription list
--------------------------
In the Aiven CLI, you can update the list of Azure subscriptions that have access to Aiven service endpoints:

.. code:: shell

    avn service privatelink azure update AIVEN_SERVICE SUBSCRIPTION_ID

Delete a Private Link service
------------------------------
Use the Aiven CLI to delete the Azure Load Balancer and Private Link service:

.. code:: shell

    avn service privatelink azure delete AIVEN_SERVICE
