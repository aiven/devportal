Set up Virtual Private Cloud peering on UpCloud
===============================================

Virtual Private Cloud (VPC) peerings enable traffic between two networks on different accounts or platforms. A peering needs to be establised from both connecting components to be activated.

Learn how to establish a VPC peering connection between Aiven and UpCloud.

About establishing Aiven-Upcloud VPC peering
--------------------------------------------

To set up a peering connection between Aiven and UpCloud, you need a VCP created for your Aiven project in `Aiven Console <https://console.aiven.io/>`_. On the UpCloud side, you need to set up the peering connection via API.

Limitations
-----------

Peering connections are only supported between networks of type ``private``.

.. important::

    Make sure you only create peerings between accounts, platforms, or networks you trust. There is no limit on what traffic can flow between the peered components. The server firewall has no effect on ``private`` type networks.

Prerequisites
-------------

* You have :doc:`created a VPC for your Aiven project <manage-vpc-peering>` in `Aiven Console <https://console.aiven.io/>`_.
* Each of the two networks to be peered has a router attached.

Set up VPC peering
------------------

Request
'''''''

.. code-block:: http

    POST /1.3/network-peering HTTP/1.1

.. code-block:: json

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
configured_status     ``active`` or ``disabled``     ``active``      no         Controls whether the peering is administratively up or down.
name                  String with length 1 to 255                    yes        Descriptive name for the peering.
network.uuid          Valid network UUID                             yes        Sets the local network of the peering.
peer_network.uuid     Valid network UUID                             yes        Sets the peer network of the peering.
===================== ============================== =============== ========== =============================================================

Expected response
'''''''''''''''''

.. code-block:: http

    HTTP/1.1 201 Created

.. code-block:: json

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

.. note::

    The above describes a response of a peering that has not been established both ways. Refer to [Get network peering details](#get-network-peering-details) for description of the states.

Error responses
'''''''''''''''

================= ======================== ===================================================
HTTP status       Error code               Description
================= ======================== ===================================================
409 Conflict      LOCAL_NETWORK_NO_ROUTER  The local network has no router.
404 Not found     NETWORK_NOT_FOUND        The local network was not found.
404 Not found     PEER_NETWORK_NOT_FOUND   Peer network was not found.
409 Conflict      PEERING_CONFLICT         The peering between these accounts already exists.
================= ======================== ===================================================
