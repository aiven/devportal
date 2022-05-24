Using Virtual Private Cloud (VPC) peering
=========================================

How to set up AWS, Google Cloud, or Azure VPC peering for Aiven projects
-------------------------------------------

Virtual Private Cloud (VPC) peering is a method of connecting separate AWS, Google Cloud, or Azure private networks with each other. This makes it possible for the virtual machines in the different VPCs to talk to each other directly without going through the public internet.

In Aiven, VPC peering is configured as a project and region-specific setting. This means that all services created and running use the same VPC peering connection. If necessary, you can use different connections for VPC peering across multiple projects.

To set up VPC peering for your Aiven project:

1. Log in to the Aiven web console.

2. Click VPC in the main menu.

3. On the right of the Project VPC view, select the cloud that you want to use for the VPC.

.. image:: /images/platform/VPC/aiven_create_project_vpc.png

4. Enter the IP range that you want to use for the VPC connection.
Use an IP range that does not overlap with any networks that you want to connect via VPC peering. For example, if your own networks use the range ``10.0.0.0/8``, you could set the range for your Aiven project's VPC to ``192.168.0.0/24``.

5. Select Create VPC.

Once you have created the VPC, Aiven automatically sets it up and updates the status in the VPC view of the web console.

When you create a new service, you can then place it in the VPC. The VPC tab in the Select Service Cloud Region section lists the available VPCs. This also allows you to migrate a service to or from a VPC.

.. Note:: Depending on the cloud provider that you selected for the VPC connection, you also have to accept a VPC peering connection request (AWS) or set up a corresponding VPC peering connection to Aiven (Google). 

Setting up the VPC peering connection in AWS 
--------------------------------------------

1. Open your AWS Console.

2. Go to My Account and make note of your account ID.

.. image:: /images/platform/VPC/aws_account_id.png

3. Go to the VPC service to find the VPC that you want to connect and copy the ID for that VPC.

4. In the Aiven web console, select the VPC connection that you created.

5. Enter your AWS account ID and VPC ID, select the region for your AWS VPC, then click Add peering connection.

.. image:: /images/platform/VPC/add_aws_peering_connection.png

This adds a new connection in your AWS Console with the Pending Acceptance status.

.. image:: /images/platform/VPC/accept_request.png

6. In your AWS Console, check that the account ID and VPC ID match those listed in the Aiven web console, then select Actions > Accept Request.
When you have accepted the request in AWS Console, the peering connection is active in the Aiven web console.

.. image:: /images/platform/VPC/aws_peering_active.png

Setting up the VPC peering connection in Google Cloud Platform (GCP)
--------------------------------------------------------------------

1. Open your GCP Console.

2. Select VPC Networks on the left and find the VPC that you want to connect.

3. Click the project name and make note of the Project ID.

4. Under GCP VPC Networks, make note of the VPC Network Name.

5. In the Aiven web console, select the VPC connection that you created.

6. Enter the project ID and VPC network name from GCP, then click Add peering connection.
This adds a new connection with the Pending Peer status.

.. image:: /images/platform/vpc/gcp_add_peering_connection.png

7. In your GCP Console, go to VPC > VPC network peering and select Create Connection.

8. Enter a name for the peering connection and enter the same project ID and network name that are shown in the Aiven web console.
You can click the blue Pending peer icon to see the Aiven project name and the network name.

9. Click Create.

.. image:: /images/platform/vpc/gcp_create_peering_connection.png

When you create the new connection, it is active in both the Aiven web console and your GCP Console.

.. image:: /images/platform/vpc/gcp_peering_active.png

Deploying new services to a VPC
-------------------------------

When you create a new service, your peered VPC is available as a new geolocation on the VPC tab.

.. image:: /images/platform/vpc/geolocation-vpc.png

.. Note:: It might take a few minutes for newly created VPCs to appear for service deployments.

Migrating a public service to a VPC
-----------------------------------

You can migrate any Aiven service to or from a VPC.

1. Log in to the Aiven web console and select your service.

2. On the Overview tab, scroll down to Cloud and VPC and click Migrate Cloud.

.. image:: /images/platform/vpc/overview-migrate-cloud.png

.. Note:: Any services that are currently public include the Public Internet status.

3. Under Region, click the VPC tab and select the VPC that you want to use.

.. image:: /images/platform/vpc/select-region-vpc.png

4. Click Migrate.
This migrates the service to the private network and sets the status to Project VPC.

.. image:: /images/platform/vpc/set-project-vpc.png

.. Note:: Once you migrate your service to an Aiven project-specific VPC, you can no longer access the service over the public internet. You can only access it from clients that are in a VPC that is peered to the VPC for the Aiven project.

Security
--------

The service nodes use firewall rules to allow only connections from private IP ranges that originate from networks on the other end of VPC peering connections. You can only deploy services to a VPC if they belong to the project where that specific VPC was created.

Accessing VPC services from the public internet
-----------------------------------------------

When you move your service to a VPC, access from public networks is blocked by default unless you switch on public access, which generates a separate endpoint with a ``public-`` prefix that you can use. You can switch on public internet access for your services in the service's Overview > Advanced Configuration section, but this option is switched off by default. 

IP filtering (the Allowed IP Addresses list on the service overview page) is still available for a service deployed to a VPC where both public and private access are allowed. We recommend that you use IP filtering when your VPC service is also exposed to the public internet.

Also note that safelisting applies to both internal and external traffic. If you safelist an external IP address and want to keep traffic flowing with the internal (peered) connections, make sure that you safelist the CIDR blocks of the peered networks as well to avoid disruptions to the service.

