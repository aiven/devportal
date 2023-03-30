Set up Virtual Private Cloud (VPC) peering on AWS
==================================================

This article provides instructions for setting up VPC peering on AWS, which you can follow after creating a :doc:`VPC on the Aiven platform <manage-vpc-peering>`.

Prerequisites
-------------

Create a :doc:`VPC on the Aiven platform <manage-vpc-peering>`.

Set up VPC peering
------------------

1. Open your AWS Console.

2. Go to **My Account** and make note of your account ID.

3. Go to the VPC service to find the VPC that you want to connect and copy the ID for that VPC.

4. In the `Aiven web console <https://console.aiven.io/>`_, select the VPC connection that you created.

5. Enter your AWS account ID and VPC ID, select the region for your AWS VPC, and select **Add peering connection**.

   .. note::
    
    As a result, a new connection  with the **Pending Acceptance** status is added in your AWS Console.

6. In your AWS Console, check that the account ID and VPC ID match those listed in the `Aiven web console <https://console.aiven.io/>`_ and, if so, select **Actions** > **Accept Request**.

7. Update `your AWS route tables <https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-routing.html>`_ to match your Aiven CIDR settings.

.. topic:: Result
    
    When you accept the request in AWS Console, the peering connection is active in the `Aiven web console <https://console.aiven.io/>`_.
