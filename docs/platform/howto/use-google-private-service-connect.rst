Use Google Private Service Connect with Aiven services 
=======================================================

.. important::

    Google Private Service Connect is a :doc:`limited availability feature </docs/platform/concepts/beta_services>`, which you can request from the sales team (sales@Aiven.io). During the limited availability stage, you can use the feature at no cost. If you want to continue using Google Private Service Connect after it reaches general availability, you'll be billed according to the latest applicable price.

    Google Private Service Connect is supported for Aiven for Apache Kafka® and Aiven for ClickHouse® only.

Discover Google Private Service Connect and benefits of using it with your Aiven services. Learn how to enable Google Private Service Connect for Aiven services.

About Private Service Connect
-----------------------------

Private Service Connect lets you bring your Aiven services into your networks (virtual private clouds) over a private endpoint. The endpoint receives a private IP address from a range that you assign. Next, connectivity over the private endpoint is routed to your Aiven service.

.. note::

   For consistency, Google Private Service Connect is called *privatelink* in Aiven tools. This applies to all clouds, including Google Cloud.

Prerequisites
-------------

Your Aiven service is hosted in :doc:`a project virtual private cloud (VPC) </docs/platform/howto/manage-vpc-peering>` in the region where the connecting endpoint will be created.

.. note::
   Private Service Connect endpoints are service specific. For each service you wish to connect to, you need to create a separate endpoint.

Set up a Private Service Connect connection
-------------------------------------------

Step 1: Enable Private Service Connect for a service
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Using the Aiven CLI, enable a Private Service Connect for your Aiven service:

.. code:: shell

    avn service privatelink google create MY_SERVICE_NAME

.. note::
   For publishing a service over Private Service Connect, a dedicated address range needs to be allocated at the publishing / Aiven end. Aiven reserves network 172.24.0.0/16 for this purpose and forbids creating project VPCs in Google Cloud overlapping with this range.

Creating a privatelink usually takes a minute or two.

You can use the following command to see the current state:

.. code:: shell

    avn service privatelink google get MY_SERVICE_NAME

When the state has changed from ``creating`` to ``active``, resources at Aiven end have been allocated, and it's possible to create connections.

When the privatelink has been successfully created, you can expect an output similar to the following:

.. code:: shell

    GOOGLE_SERVICE_ATTACHMENT                                                             STATE
    ====================================================================================  ======
    projects/aivenprod/regions/europe-west1/serviceAttachments/privatelink-s3fd836dfc60   active

.. note::
   The GOOGLE_SERVICE_ATTACHMENT value is used to connect an endpoint on the client side to the Aiven service.

Step 2: Create a Private Service Connect connection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can now create an PSC endpoint and connection to the Aiven service within the `Google Console <https://console.cloud.google.com/net-services/psc/addConsumer>`_.

1. Select **Published service** as **Target type**.

   .. note::
      **Target service** should be the GOOGLE_SERVICE_ATTACHMENT value/URI from the previous step.

2. Select an existing subnet hosting your side of the endpoint.

After the endpoint is created, it initially exists in the ``pending`` state. To allow connections via the endpoint, it needs to be accepted at the service publisher (Aiven) end.

.. tip::
   If you use an automatically-assigned IP address, note the IP address associated with the endpoint so that you can use it the next step.

Step 3: Approve the created connection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Update the state of Private Service Connect connections for your Aiven service by running

.. code:: shell

    avn service privatelink google refresh MY_SERVICE_NAME

2. Retry the following command until it returns the pending-user-approval status:

.. code:: shell

    avn service privatelink google connection list MY_SERVICE_NAME

.. code:: shell

    PRIVATELINK_CONNECTION_ID  PSC_CONNECTION_ID  STATE                  USER_IP_ADDRESS
    =========================  =================  =====================  ===============
    plc3fd852bec98             12870921937223780  pending-user-approval  null

.. note::
   * PSC_CONNECTION_ID is the identifier assigned to Google for the connection, and you can use it to verify that the connection is indeed matching your Private Service Connect endpoint.
   * PRIVATELINK_CONNECTION_ID is an Aiven internal identifier for the connection, which is needed in the final connection approval step.

3. To enable a connection, approve it.

.. note::
    By approving the connection, you provide the IP address assigned to your PSC endpoint - whether automatically assigned or static. Aiven uses this IP address for pointing the service DNS records necessary for the clients to reach the Aiven service through the Private Service Connect connection.

To approve the connection, run the following approval command:

.. code:: shell

    avn service privatelink google connection approve MY_SERVICE_NAME --privatelink-connection-id PRIVATELINK_CONNECTION_ID --user-ip-address PSC_ENDPOINT_IP_ADDRESS

As a result, the connection initially transitions to the user-approved state.

.. code:: shell

    avn service privatelink google connection list MY_SERVICE_NAME

.. code:: shell

    PRIVATELINK_CONNECTION_ID  PSC_CONNECTION_ID  STATE          USER_IP_ADDRESS
    =========================  =================  =============  ===============
    plc3fd852bec98             12870921937223780  user-approved  10.0.0.100

You may be need to run the ``avn service privatelink google refresh`` command at this point since updates to service attachment accept lists are not immediately reflected in the states of returned connected endpoints.

.. code:: shell

    avn service privatelink google refresh MY_SERVICE_NAME

After establishing the connection and populating DNS records , the connection appears as ``active``.

.. code:: shell

    avn service privatelink google connection list MY_SERVICE_NAME

.. code:: shell

    PRIVATELINK_CONNECTION_ID  PSC_CONNECTION_ID  STATE   USER_IP_ADDRESS
    =========================  =================  ======  ===============
    plc3fd852bec98             12870921937223780  active  10.0.0.100

The state of your Private Service Connect endpoint should have transitioned from ``pending`` to ``accepted`` at this point. Private Service Connect connectivity has been established now.

As the final step, you need to allow connectivity using the Private Service Connect endpoint.

Step 4: Enable Private Link access service components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Finally, enable Private Link access on your Aiven services using either the :doc:`Aiven CLI </docs/tools/cli>` or `Aiven Console <https://console.aiven.io/>`_.

**Aiven CLI**

To enable Private Service Connect access for your service in the Aiven CLI, set ``user_config.privatelink_access.<service component>`` to ``true`` for the components you want to enable. Take the following command as an example for Apache Kafka:

.. code:: shell

    avn service update -c privatelink_access.kafka=true MY_SERVICE_NAME

**Aiven Console**

To enable Private Link access in `Aiven Console <https://console.aiven.io/>`_, take the following steps:

1. Select the service that you want to enable access to.
2. On the **Overview** page of your service, in the **Advanced configuration** section, select **Change**.
3. Select **Add configuration option**, and select the ``privatelink_access.<service component>`` option for the components that you want to enable.
4. Toggle the switch next to the components to set the values to ``true``.
5. Select **Save advanced configuration**.

.. Tip::

    Each service component can be controlled separately. For example, you can enable Private Service Connect access for your Aiven for Apache Kafka® service while allowing Kafka® Connect to only be connected via VNet peering.

Acquire connection information
------------------------------

One Private Service Connect connection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have one private endpoint connected to your Aiven service, you can preview the connection information (URI, hostname, or port required to access the service through the private endpoint) in `Aiven Console <https://console.aiven.io/>`_ > the service's **Overview** page > the **Connection information** section, where you'll also find the switch for the ``privatelink`` access route. ``privatelink``-access-route values for ``host`` and ``port`` differ from those for the ``dynamic`` access route used by default to connect to the service.

Multiple Private Service Connect connections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use CLI to acquire connection information for more than one Private Service Connect connection.

Each endpoint (connection) has PRIVATELINK_CONNECTION_ID, which you can check using the :doc:`avn service privatelink google connection list SERVICE_NAME </docs/tools/cli/service/privatelink>` command.

To acquire connection information for your service component using Private Service Connect, run the :doc:`avn service connection-info </docs/tools/cli/service/connection-info>` command.

* For SSL connection information for your service component using Private Service Connect, run the following command:

.. code-block:: bash

   avn service connection-info UTILITY_NAME SERVICE_NAME -p PRIVATELINK_CONNECTION_ID

.. topic:: Where

  * UTILITY_NAME is ``kcat``, for example
  * SERVICE_NAME is ``kafka-12a3b4c5``, for example
  * PRIVATELINK_CONNECTION_ID is ``plc39413abcdef``, for example

* For SASL connection information for Aiven for Apache Kafka® service components using using Private Service Connect, run the following command:

.. code-block:: bash

   avn service connection-info UTILITY_NAME SERVICE_NAME -p PRIVATELINK_CONNECTION_ID -a sasl

.. topic:: Where

  * UTILITY_NAME is ``kcat``, for example
  * SERVICE_NAME is ``kafka-12a3b4c5``, for example
  * PRIVATELINK_CONNECTION_ID is ``plc39413abcdef``, for example

.. note::

   SSL certificates and SASL credentials are the same for all the connections.

Delete a Private Link service
------------------------------
Use the :doc:`Aiven CLI </docs/tools/cli>` to delete the Private Service Connect connection for a service:

.. code:: shell

    avn service privatelink google delete MY_SERVICE_NAME
