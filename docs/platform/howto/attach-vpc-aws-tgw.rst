Attach VPC to AWS Transit Gateway
=================================

`AWS Transit Gateway (TGW) <https://aws.amazon.com/transit-gateway/>`_ enables transitive routing from on-premises networks through VPN and from other VPC. 
By creating a Transit Gateway VPC attachment, services in an Aiven Project VPC can route traffic to all other networks attached - directly or indirectly - to the Transit Gateway.

Set up a project VPC
--------------------

Create a VPC on the Aiven platform in the same region as your Transit Gateway.

Set up a VPC attachment for your Project VPC
------------------------------------------------

Install the Aiven CLI
~~~~~~~~~~~~~~~~~~~~~

These instructions apply to the :doc:`Aiven CLI </docs/tools/cli>`, but the same configuration can also be managed using the Aiven web console.

Locate your AWS account and AWS Transit Gateway ID
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To attach a VPC to a Transit Gateway in a different account, the AWS account ID must be included. 
This ID is 12-digits and will be referred to below as ``$user_account_id``.
In addition the ID of the Transit Gateway itself is needed. This has the format ``tgw-...`` with the dots being 17 hexadecimal characters.
It will be referred to as ``$user_tgw_id``.

Share the AWS Transit Gateway with the Aiven AWS account
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before the Aiven platform can attach the Project VPC located in the Aiven AWS account with the Transit Gateway in your account, the TGW needs to be shared using `AWS Resource Access Manager <https://aws.amazon.com/ram/>`_. 
Sharing the TGW allows the Aiven account to describe the TGW and its route table(s), and to request attaching VPC (and VPN) to it. Note that attachments are not automatically created when the VPC and TGW reside in different accounts - the TGW owner account needs to accept a VPC attachment, similar to how VPC peering connections are before they become ``available``.

A resource share can be created using the `AWS RAM console <https://console.aws.amazon.com/ram/home>`_, or the `AWS CLI <https://aws.amazon.com/cli/>`_ using the `create-resource-share <https://docs.aws.amazon.com/cli/latest/reference/ram/create-resource-share.html>`_ command. Please add the Transit Gateway as a resource to the share, and the Aiven AWS account ID as a principal. The Aiven AWS account ID is ``675999398324``.

Find your project VPC ID
~~~~~~~~~~~~~~~~~~~~~~~~

Use ``avn vpc list`` to find the ID for your Project VPC. The ``project_vpc_id value`` (a UUID4 string) will be referred to as ``$project_vpc_id`` later.

Determine the IP ranges to route from the Project VPC to the AWS Transit Gateway
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

While a Transit Gateway has a route table of its own, and will by default route traffic to each attached network (directly to attached VPC or indirectly via VPN attachments), the attached route tables of the VPC need to be updated to include the TGW as a target for any IP range (CIDR) that should be routed using the VPC attachment. These IP ranges must be configured when creating the attachment for an Aiven Project VPC.
The IPv4 range will be referred below to as ``$user_peer_network_cidr``.

Create Aiven peering connection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A Transit Gateway VPC attachment is created by making a request to the Aiven API for a peering connection. The Aiven API handles both actual `AWS VPC peering connections <https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html>`_ and AWS Transit Gateway VPC attachments as peering connections.

.. code-block:: shell

    avn vpc peering-connection create \
      --project-vpc-id $aws_vpc \
      --peer-cloud-account $user_account_id \
      --peer-vpc $user_tgw_id \
      --user-peer-network-cidr $user_peer_network_cidr

Note that you can use the ``--user-peer-network-cidr`` argument multiple times to define more than one peer network CIDR. It's also possible to create the attachment without any CIDRs and add them later (though the attachment will be not be of any use until that is done since no addresses will be routed through the TGW from the Project VPC).

Accept AWS Transit Gateway VPC attachment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After running ``vpc peering-connection create`` command the state of the Aiven peering connection is ``APPROVED``. Once the Aiven platform has built the connection by creating an AWS Transit Gateway VPC attachment, the state changes to ``PENDING_PEER`` if everything went well. Otherwise the state information will indicate why the attachment failed to be created. Note that it may take up to a few minutes before building the attachment has completed.

The state can be checked using:

.. code-block:: shell

    avn vpc peering-connection \
      --project-vpc-id $project_vpc_id \
      --peer-cloud-account $user_account_id \
      --peer-vpc $user_tgw_id -v

Once the state is ``PENDING_PEER``, the output will contain a message instructing to accept a VPC attachment in your AWS account. The Aiven platform monitors the attachment until it has been accepted, and once that is detected the state changes to ``ACTIVE`` indicating the VPC attachment is operational, the Project VPC route table has been updated to route ``$user_peer_network_cidr`` to the Transit Gateway, and service nodes in the Project VPC have opened firewall access to those networks.
