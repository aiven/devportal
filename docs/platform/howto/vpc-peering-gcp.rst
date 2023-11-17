Set up Virtual Private Cloud (VPC) peering on Google Cloud Platform (GCP)
=========================================================================

Once you've created a :doc:`VPC on the Aiven platform <manage-vpc-peering>`, you can follow these instructions to set up VPC peering on GCP.

1. Open your GCP Console.

2. Select **VPC Networks** and find the VPC that you want to connect to.

3. Click the project name, and make note of the **Project ID**.

4. Under **VPC Network**, make note of the **VPC Network Name**.

5. In `Aiven Console <https://console.aiven.io>`_, select **VPCs** from the sidebar on the **Services** page.

6. On the **Virtual private clouds** page, select the VPC connection that you created.

7. In the **VPC Peering connections** view, enter the GCP project ID (step 3) into the **GCP project ID** field and the exact GCP VPC network name (step 4) into the **GCP VPC network name** field. Next, select **Add peering connection**.

   This adds a new connection with the *Pending Peer* status.

   .. note::

      Select the blue **Pending peer** icon, and make a note of the Aiven project ID and the VPC network name.

8. In your GCP Console, go to **VPC** > **VPC network peering**, and select **Create peering connection**.

9. To create a peering connection, take the following steps:

   1. Enter a name for the peering connection.
   2. Under **Peered VPC network**, select **In another project**.
   3. Enter the Aiven project ID and the VPC network name identified in step 7 in Aiven Console.

10. Click **Create**.

When the peering is successful, it is active in both `Aiven Console <https://console.aiven.io>`_ and your GCP Console.
