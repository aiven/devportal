Set Virtual Private Cloud (VPC) peering on AWS
==============================================

Once you've created a :doc:`VPC on the Aiven platform <docs/platform/howto/manage-vpc-peering>`, you can follow this instruction to set up VPC peering on AWS.

1. Open your AWS Console.

2. Go to **My Account** and make note of your account ID.

3. Go to the VPC service to find the VPC that you want to connect and copy the ID for that VPC.

4. In the Aiven web console, select the VPC connection that you created.

5. Enter your AWS account ID and VPC ID, select the region for your AWS VPC, then click **Add peering connection**.
This adds a new connection in your AWS Console with the Pending Acceptance status.

6. In your AWS Console, check that the account ID and VPC ID match those listed in the Aiven web console, then select **Actions** > **Accept Request**.

When you have accepted the request in AWS Console, the peering connection is active in the Aiven web console.
