Set up AWS Marketplace for Aiven services
===========================================

Aiven makes its services available through the Amazon AWS Marketplace. This article shows the steps needed to create a subscription that links the accounts.

First, there are some steps that need to be completed on the AWS Marketplace page before heading over to the Aiven Console and finishing the process.

AWS Marketplace setup
---------------------

1. Search for "Aiven Managed Database Services" on the `AWS Marketplace <https://aws.amazon.com/marketplace/pp/prodview-vylwtm6t2c7fk>`_.  This page contains information about all of Aiven's services and how the marketplace subscription works.  Click the **View purchase options** button on this page.

.. image:: /images/platform/howto/aws-marketplace-listing.png
   :alt: AWS Marketplace purchase options button for Aiven Managed Database Services

2. When you are ready, click the **Subscribe** button on the page. You will NOT be charged by clicking this button; this only sets up a billing subscription between AWS and Aiven. You will only be charged after deploying Aiven services.

3. Click **Set up your account**.  This takes you to the Aiven Console to complete the process.

Aiven account setup
-------------------

4. You should now be on the AWS signup page at Aiven, asking you to sign up or log in. 

5. After registering or logging in, choose or create an Aiven organization to use the AWS subscription for. If you have any existing Aiven projects that you want to be moved to this AWS subscription, this organization name is the one you will need for that.

If you have any issues linking Aiven to your AWS subscription, you can try the process again in the AWS web console by finding the Aiven subscription and clicking **Set up your account**.


.. note:: 
    The URL that you log in to for your AWS subscription is https://console.aws.aiven.io. This is different from the Aiven Console (https://console.aiven.io). 


