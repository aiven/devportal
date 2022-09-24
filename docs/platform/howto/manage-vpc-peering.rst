.. _platform_howto_setup_vpc_peering:

Manage Virtual Private Cloud (VPC) peering
==========================================

Virtual Private Cloud (VPC) peering is a method of connecting separate AWS, Google Cloud, or Azure private networks with each other. This makes it possible for the virtual machines in the different VPC to talk to each other directly without going through the public internet.

In Aiven, VPC peering is configured as a project and region-specific setting. This means that all services created and running use the same VPC peering connection. If necessary, you can use different connections for VPC peering across multiple projects.

To set up VPC peering for your Aiven project:

1. Log in to the Aiven web console.

2. Click **VPC** in the main menu.

3. On the right, click **Create VPC** button.

   .. note::
       You'll need either an **admin** or an **operator** user role to be able to create a VPC. For more information about Aiven project members and roles, refer to :doc:`../concepts/projects_accounts_access`.  

4. Enter the IP range that you want to use for the VPC connection.
Use an IP range that does not overlap with any networks that you want to connect via VPC peering. For example, if your own networks use the range 10.0.0.0/8, you could set the range for your Aiven project's VPC to 192.168.0.0/24.

5. Click **Create VPC**.

Once you have created the VPC, Aiven automatically sets it up and updates the status in the **VPC** view of the web console.

When you create a new service, you can then place it in the VPC. The **VPC** tab in the *Select Service Cloud Region* section lists the available VPC. This also allows you to migrate a service to or from a VPC.

   .. note::
       Depending on the cloud provider that you selected for the VPC connection, you also have to accept a VPC peering connection request or set up a corresponding VPC peering connection to Aiven. 

Cloud-specific VPC peering instructions
-----------------------------------------------------

- Refer to :ref:`GCP VPC peering instructions <vpc-peering-gcp>`.

Deploying new services to a VPC
-------------------------------

When you create a new service, your peered VPC is available as a new geolocation on the **VPC** tab under *Select Service Cloud Region*.
It might take a few minutes for newly created VPC to appear for service deployments.

.. note::

The service nodes use firewall rules to allow only connections from private IP ranges that originate from networks on the other end of VPC peering connections. You can only deploy services to a VPC if they belong to the project where that specific VPC was created.

Deleting an existing VPC and VPC peering
----------------------------------------

Before deleting an existing VPC from Aiven console, you should move out any active services from that VPC. To delete a VPC, navigate to the Aiven console under the VPC section. You can find the **Delete** button as the last column for each VPC.
Once the VPC is deleted, the cloud provider side of the peering connection will go to an inactive or deleted state.

Migrating a public service to a VPC
-----------------------------------

You can migrate any Aiven service to or from a VPC.

1. Log in to the Aiven web console and select your service.

2. On the *Overview* tab, scroll down to *Cloud and VPC* and click **Migrate Cloud**.

   .. note::
       Any services that are currently public include the *Public Internet* status.

3. Under Region, click the **VPC** tab and select the VPC that you want to use.

4. Click **Migrate**. This migrates the service to the private network and sets the status to *Project VPC*.

   .. note::
       Once you migrate your service to an Aiven project-specific VPC, you can no longer access the service over the public internet. You can only access it from clients that are in a VPC that is peered to the VPC for the Aiven project.


Accessing VPC services from the public internet
-----------------------------------------------

When you move your service to a VPC, access from public networks is blocked by default unless you switch on public access, which generates a separate endpoint with a public- prefix that you can use.
You can switch on public internet access for your services in the service's *Overview* > *Advanced Configuration* section, but this option is switched off by default. As an example, see :doc:`how to enable public access in a VPC <public-access-in-vpc>`.

IP filtering (the Allowed IP Addresses list on the service overview page) is still available for a service deployed to a VPC where both public and private access are allowed. We recommend that you use IP filtering when your VPC service is also exposed to the public internet.

Also note that safelisting applies to both internal and external traffic. If you safelist an external IP address and want to keep traffic flowing with the internal (peered) connections, make sure that you safelist the CIDR blocks of the peered networks as well to avoid disruptions to the service.

