Manage Virtual Private Cloud (VPC) peering
==========================================

Virtual Private Cloud (VPC) peering is a method of connecting separate AWS, Google Cloud, or Azure private networks with each other. This makes it possible for the virtual machines in the different private networks to talk to each other directly without going through the public internet.

.. _platform_howto_setup_vpc_peering:

Configure VPC peering
----------------------------------------

In Aiven, VPC peering is configured as a project and region-specific setting. This means that all services created and running use the same VPC peering connection. If necessary, you can use different connections for VPC peering across multiple projects.

To set up VPC peering for your Aiven project:

1. In Aiven Console, click **VPC**.

2. Click **Create VPC**.

   .. note::

       **Admin** and **operator** user roles can create a VPC. For more information about Aiven project members and roles, refer to :doc:`Organizations, projects, and managing access permissions </docs/platform/concepts/projects_accounts_access>`.  

3. Enter the IP range that you want to use for the VPC connection.  Use an IP range that does not overlap with any networks that you want to connect via VPC peering. For example, if your own networks use the range `10.0.0.0/8`, you could set the range for your Aiven project's VPC to `192.168.0.0/24`.

4. Click **Create VPC**.

The state of the VPC is shown in the table.

Cloud-specific VPC peering instructions
----------------------------------------

- :doc:`Set up VPC peering on Amazon Web Services (AWS) </docs/platform/howto/vpc-peering-aws>`
- :doc:`Set up VPC peering on Google Cloud Platform (GCP) </docs/platform/howto/vpc-peering-gcp>`
- :doc:`Set up VNet (VPC) peering on Microsoft Azure </docs/platform/howto/vnet-peering-azure>`

.. note::

       Depending on the cloud provider that you selected for the VPC connection, you also have to accept a VPC peering connection request or set up a corresponding VPC peering connection to Aiven. 

Deploy new services to a VPC
-------------------------------

When you create a new service, your peered VPC is available as a new geolocation on the **VPC** tab under **Select Service Cloud Region**. It can take a few minutes for a newly created VPC to appear for service deployments.

.. note::

       The service nodes use firewall rules to allow only connections from private IP ranges that originate from networks on the other end of VPC peering connections. You can only deploy services to a VPC if they belong to the project where that specific VPC was created.

Delete an existing VPC and VPC peering
----------------------------------------

Before deleting an existing VPC from Aiven console, you should move out any active services from that VPC. To delete a VPC, navigate to the Aiven console under the VPC section. You can find the **Delete** button as the last column for each VPC.
Once the VPC is deleted, the cloud provider side of the peering connection will go to an inactive or deleted state.

Migrate a public service to a VPC
-----------------------------------

You can migrate any Aiven service to a different VPC:

#. In Aiven Console, go to your service.

#. On the **Overview** tab in the **Cloud and VPC** section, click **Migrate Cloud**.

#. In the **Region** section, select the **VPC** tab.

#. Select the VPC that you want to use.

#. Click **Migrate**. 

Access VPC services from the public internet
-----------------------------------------------

When you move your service to a VPC, access from public networks is blocked by default. If you switch to public access, a separate endpoint is created with a public prefix. 
You can enable public internet access for your services by following the :doc:`Enable public access in a VPC </docs/platform/howto/public-access-in-vpc>` instructions.

IP filtering (the Allowed IP Addresses list on the service overview page) is still available for a service deployed to a VPC where both public and private access are allowed. We recommend that you use IP filtering when your VPC service is also exposed to the public internet.

Also note that safelisting applies to both internal and external traffic. If you safelist an external IP address and want to keep traffic flowing with the internal (peered) connections, make sure that you safelist the CIDR blocks of the peered networks as well to avoid disruptions to the service.

Troubleshoot VPC connection issues
-------------------------------------

Any network changes to VPC peered hosts external from Aiven can cause issues with routing to your Aiven services hosted in a VPC. To troubleshoot such issues, take the following steps:

1. In `Aiven Console <https://console.aiven.io/>`_, select **VPC**.
2. Find the ID of the affected VPC and select it from the **Internal ID** column.
3. Select **Refresh VPC connections**.

As a result, the platform checks the VPC peering connection and rebuilds the peering connection state if there are any changes detected.

For any other issues, open a support ticket from Aiven Console to get in touch with the support team and/or see :doc:`Get support in the Aiven Console </docs/platform/howto/project-support-center>`.