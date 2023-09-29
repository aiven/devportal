Set up SDN network peering between Aiven and UpCloud
====================================================

SDN network peerings enable traffic between two networks on different accounts or platforms. A peering needs to be established from both connecting components to be activated.

This article shows how to establish a network peering connection between Aiven and UpCloud.

About establishing Aiven-Upcloud peering
----------------------------------------

To set up a peering connection between Aiven and UpCloud, you need a VPC created for your Aiven project in `Aiven Console <https://console.aiven.io/>`_. On the UpCloud side, you can set up the peering connection via API. Since the API takes UUIDs of both networks as attrbutes, you need to identify the network UUIDs before calling the API.

Limitations
-----------

Peering connections are only supported between networks of type ``private``.

.. important::

    Make sure you only create peerings between accounts, platforms, or networks you trust. There is no limit on what traffic can flow between the peered components. The server firewall has no effect on ``private`` type networks.

Prerequisites
-------------

* You have :doc:`created a VPC for your Aiven project <manage-vpc-peering>` in `Aiven Console <https://console.aiven.io/>`_.
* Each of the two networks to be peered has a router attached.

Identify networks' UUIDs
------------------------

Before establishing a peering connection with the UpCloud API, you need to find UUIDs for each of the two networks to be peered.

UpCloud SDN network UUID
''''''''''''''''''''''''

Aiven VPC network UUID
''''''''''''''''''''''

1. In `Aiven Console <https://console.aiven.io/>`_, select **VPCs** from the sidebar on the **Services** page.

2. On the **Virtual private clouds** page, select the VPC connection that you created.

3. On the **VPC Peering connections** page, enter your AWS account ID and VPC ID, select the region for your AWS VPC, and select **Add peering connection**.

   .. note::
    
    As a result, a new connection with the **Pending Acceptance** status is added in your AWS Console.

4. In your AWS Console, check that the account ID and VPC ID match those listed in the `Aiven Console <https://console.aiven.io/>`_ and, if so, select **Actions** > **Accept Request**.

Set up VPC peering
------------------

To establish a VPC peering from UpCloud to Aiven, use `UpCloud API <https://developers.upcloud.com/1.3/>`_ to send the following request:

.. code-block:: bash

    POST /1.3/network-peering HTTP/1.1
    {
      "network_peering": {
        "configured_status": "active",
        "name": "Peering A->B",
        "network": {
          "uuid": "03126dc1-a69f-4bc2-8b24-e31c22d64712"
        },
        "peer_network": {
          "uuid": "03585987-bf7d-4544-8e9b-5a1b4d74a333"
        }
      }
    }

Attributes
''''''''''

===================== ============================== =============== ========== =============================================================
Attribute             Accepted values                Default value   Required   Description
===================== ============================== =============== ========== =============================================================
``configured_status`` ``active`` or ``disabled``     ``active``      No         Controls whether the peering is administratively up or down.
``name``              String of 1-255 characters                     Yes        Descriptive name for the peering
``network.uuid``      Valid network UUID                             Yes        Sets the local network of the peering.
``peer_network.uuid`` Valid network UUID                             Yes        Sets the peer network of the peering.
===================== ============================== =============== ========== =============================================================

Expected response
'''''''''''''''''

.. note::

    The sample response provided describes a peering established one way only.

.. code-block:: bash

    HTTP/1.1 201 Created
    {
      "network_peering": {
        "configured_status": "active",
        "name": "Peering A->B",
        "network": {
          "ip_networks": {
            "ip_network": [
              {
                "address": "192.168.0.0/24",
                "family": "IPv4"
              },
              {
                "address": "fc02:c4f3::/64",
                "family": "IPv6"
              }
            ]
          },
          "uuid": "03126dc1-a69f-4bc2-8b24-e31c22d64712"
        },
        "peer_network": {
          "uuid": "03585987-bf7d-4544-8e9b-5a1b4d74a333"
        },
        "state": "pending-peer",
        "uuid": "0f7984bc-5d72-4aaf-b587-90e6a8f32efc"
      }
    }

Error responses
'''''''''''''''

================= ======================== ===================================================
HTTP status       Error code               Description
================= ======================== ===================================================
409 Conflict      LOCAL_NETWORK_NO_ROUTER  The local network has no router.
404 Not found     NETWORK_NOT_FOUND        The local network was not found.
404 Not found     PEER_NETWORK_NOT_FOUND   The peer network was not found.
409 Conflict      PEERING_CONFLICT         The peering already exists.
================= ======================== ===================================================
