Set up network peering between Aiven and UpCloud
================================================

Network peerings enable traffic between two networks from different accounts or platforms. A peering needs to be established from both connecting components to be activated.

This article shows how to establish a network peering connection between Aiven and UpCloud.

About establishing Aiven-Upcloud peering
----------------------------------------

Peering Aiven and UpCloud networks requires establishing the connection on both ends: Aiven and UpCloud.

* To set up a peering from Aiven to UpCloud, you can use `Aiven Console <https://console.aiven.io/>`_ to create a VPC for your Aiven project and add a peering connection to UpCloud. For this purpose, you need to identify the UpCloud SDN network UUID first.
* To set up a peering from UpCloud to Aiven, you can use `UpCloud API <https://developers.upcloud.com/1.3/>`_. Since the API takes UUIDs of both networks as attributes, you need to identify the network UUIDs before calling the API.

Limitations
-----------

* Peering connections are only supported between networks of type ``private``.
* You cannot initiate a peering between two networks with overlapping CIDR ranges.
* The networks to be peered need to be in the same cloud zone.

.. important::

    Make sure you only create peerings between accounts, platforms, or networks you trust. There is no limit on what traffic can flow between the peered components. The server firewall has no effect on ``private`` type networks.

Prerequisites
-------------

* You have :doc:`created a VPC for your Aiven project <manage-vpc-peering>` in `Aiven Console <https://console.aiven.io/>`_.
* CIDR ranges of the networks you want to peer do not overlap.

.. _upcloud-uuid:

Get UpCloud SDN network UUID
----------------------------

Before establishing a peering connection from Aiven to UpCloud, you need to find your UpCloud SDN network UUID.

To check the UpCloud SDN network UUID, send a request to `get network details <https://developers.upcloud.com/1.3/13-networks/#get-network-details>`_ UpCloud API endpoint. In the response, you'll get the network's UUID.

.. _avn-uuid:

Set up VPC peering from Aiven
-----------------------------

You can establish a peering connection from Aiven to UpCloud using `Aiven Console <https://console.aiven.io/>`_.

1. Log in to `Aiven Console <https://console.aiven.io/>`_, navigate to the organization and project you want to use.
2. On the **Services** page, select **VPCs** from the sidebar.
3. On the **Virtual private clouds** page, select the ID of the VPC connection you want to use for the peering.
4. On the **VPC peering connections** page, in the **Add peering connection** section, populate **Peer network ID** field with your UpCloud SDN network UUIDs.
5. Select **Add peering connection**. This adds a new connection to the VPC peering connections list.
6. Wait until you see the ``peer_pending`` state in the **State** column of the of the VPC peering connections table. At this point, the Aiven VPC network UUID should be available in the **Aiven network ID** column of the of the VPC peering connections table.

Set up VPC peering from UpCloud
-------------------------------

To establish a VPC peering from UpCloud to Aiven, use `UpCloud API <https://developers.upcloud.com/1.3/>`_ to send the following request:

.. code-block:: bash

    POST /1.3/network-peering HTTP/1.1
    {
      "network_peering": {
        "configured_status": "active",
        "name": "NAME_OF_YOUR_PEERING",
        "network": {
          "uuid": "UPCLOUD_SDN_NETWORK_UUID"
        },
        "peer_network": {
          "uuid": "AIVEN_VPC_NETWORK_UUID"
        }
      }
    }

Attributes
''''''''''

===================== ============================== =============== ========== ======================================================================================================================= ========================================
Attribute             Accepted value                 Default value   Required   Description                                                                                                             Example value
===================== ============================== =============== ========== ======================================================================================================================= ========================================
``configured_status`` ``active`` or ``disabled``     ``active``      No         Controls whether the peering is administratively up or down.                                                            ``active``
``name``              String of 1-255 characters     None            Yes        Descriptive name for the peering                                                                                        ``peering upcloud->aiven``
``network.uuid``      Valid network UUID             None            Yes        Sets the local network of the peering. Use the UUID you acquired in :ref:`Get UpCloud SDN network UUID <upcloud-uuid>`. ``03126dc1-a69f-4bc2-8b24-e31c22d64712``
``peer_network.uuid`` Valid network UUID             None            Yes        Sets the peer network of the peering. Use the UUID you acquired in :ref:`Set up VPC peering from Aiven <avn-uuid>`.     ``03585987-bf7d-4544-8e9b-5a1b4d74a333``
===================== ============================== =============== ========== ======================================================================================================================= ========================================

Expected response
'''''''''''''''''

.. note::

    The sample response provided describes a peering established one way only.

If your peering API request is successful, you can expect a response similar to the following:

.. code-block:: bash

    HTTP/1.1 201 Created
    {
      "network_peering": {
        "configured_status": "active",
        "name": "NAME_OF_YOUR_PEERING",
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
          "uuid": "UPCLOUD_SDN_NETWORK_UUID"
        },
        "peer_network": {
          "uuid": "AIVEN_VPC_NETWORK_UUID"
        },
        "state": "pending-peer",
        "uuid": "PEERING_UUID"
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

Related reading
---------------

* :doc:`Manage Virtual Private Cloud (VPC) peering </docs/platform/howto/manage-vpc-peering>`
* :doc:`Set up Virtual Private Cloud (VPC) peering on AWS </docs/platform/howto/vpc-peering-aws>`
* :doc:`Set up Virtual Private Cloud (VPC) peering on Google Cloud Platform (GCP) </docs/platform/howto/vpc-peering-gcp>`
* :doc:`Set up Azure virtual network peering </docs/platform/howto/vnet-peering-azure>`
