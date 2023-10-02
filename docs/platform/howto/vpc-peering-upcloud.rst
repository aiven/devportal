Set up network peering between Aiven and UpCloud
================================================

Network peerings enable traffic between two networks from different accounts or platforms. A peering needs to be established from both connecting components to be activated.

This article shows how to establish a network peering connection between Aiven and UpCloud.

About establishing Aiven-Upcloud peering
----------------------------------------

To set up a peering connection between Aiven and UpCloud, you need a VPC created for your Aiven project in `Aiven Console <https://console.aiven.io/>`_. On the UpCloud side, you can set up the peering connection via API. Since the API takes UUIDs of both networks as attributes, you need to identify the network UUIDs before calling the API.

Limitations
-----------

* Peering connections are only supported between networks of type ``private``.
* You cannot initiate a peering between two networks with overlapping CIDR ranges.

.. important::

    Make sure you only create peerings between accounts, platforms, or networks you trust. There is no limit on what traffic can flow between the peered components. The server firewall has no effect on ``private`` type networks.

Prerequisites
-------------

* You have :doc:`created a VPC for your Aiven project <manage-vpc-peering>` in `Aiven Console <https://console.aiven.io/>`_.
* Make sure that CIDR ranges of the networks you want to peer do not overlap.

Identify networks' UUIDs
------------------------

Before establishing a peering connection with the UpCloud API, you need to find UUIDs for each of the two networks to be peered.

UpCloud SDN network UUID
''''''''''''''''''''''''

To check the UpCloud SDN network UUID, send a request to `get network details <https://developers.upcloud.com/1.3/13-networks/#get-network-details>`_ UpCloud API endpoint. In the response, you'll get the network's UUID.

Aiven VPC network UUID
''''''''''''''''''''''

You can check the Aiven VPC network UUID in `Aiven Console <https://console.aiven.io/>`_.

1. Log in to `Aiven Console <https://console.aiven.io/>`_, navigate to the organization and project you want to use.
2. On the **Services** page, select **VPCs** from the sidebar.
3. On the **Virtual private clouds** page, select the ID of the VPC connection you want to use for the peering.
4. On the **VPC peering connections** page, in the **Add peering connection** section, populate **Network ID** field with your UpCloud SDN network UUIDs.
5. Select **Add peering connection**. This adds a new connection to the VPC peering connections list.
6. Wait until you see the ``peer_pending`` state in the **State** column of the of the VPC peering connections list. At this point, the Aiven VPC network UUID should show up as ``state_info`` right next to the state itself.

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
