.. _vpc-peering-gcp:

Set up Virtual Private Cloud (VPC) peering on Google Cloud Platform (GCP)
======================================================================

Once you've created a :ref:`VPC on the Aiven platform <platform_howto_setup_vpc_peering>`, you can follow this instruction to set up VPC peering on AWS.

1. Open your GCP Console.

2. Select **VPC Networks** on the left and find the VPC that you want to connect.

3. Click the project name and make note of the *Project ID*.

4. Under *VPC Networks*, make note of the VPC Network Name.

5. In the Aiven web console, select the VPC connection that you created.

6. Enter the project ID and VPC network name from GCP, then click **Add peering connection**.
This adds a new connection with the *Pending Peer* status.

7. In your GCP Console, go to **VPC** > **VPC network peering** and select **Create Connection**.

8. Enter a name for the peering connection and enter the same project ID and network name that are shown in the Aiven web console.

   .. note::
       You can click the blue Pending peer icon to see the Aiven project name and the network name.

9. Click **Create**.

When the peering is successful, it is active in both the Aiven web console and your GCP Console.
