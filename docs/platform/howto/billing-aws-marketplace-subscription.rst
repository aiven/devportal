Set up AWS Marketplace for Aiven services
===========================================

Aiven makes its services available through the Amazon AWS Marketplace. This article shows the steps needed to create a subscription that links the accounts.

First, there are some steps that need to be completed on the AWS Marketplace page before heading over to the Aiven Console and finishing the process.

AWS Marketplace setup
---------------------

1. Search for "Aiven Managed Database Services" on the `AWS Marketplace <https://aws.amazon.com/marketplace/pp/prodview-vylwtm6t2c7fk>`_.  This page contains information about all of Aiven's services and how the marketplace subscription works.  Click the **View purchase options** button on this page.

.. image:: /images/platform/howto/aws-marketplace-listing.png
   :alt: AWS Marketplace purchase options button for Aiven Managed Database Services

2. When you are ready, click the **Subscribe** button on the page.  You will NOT be charged by clicking this button; this only sets up a billing subscription between AWS and Aiven.  You will only be charged after deploying Aiven services.

3. You should now see a button inviting you to "Set up your account".  This will take you to the Aiven website to complete the process; proceed to step 4 below.

Aiven account setup
-------------------

4. You should now be on the AWS signup page at Aiven, asking you to sign up or log in.  As this is probably your first visit to Aiven via the AWS subscription, choose the "Sign up" button.

5. After entering your email address and completing the registration, you will be able to log in to the `Aiven AWS console <https://console.aws.aiven.io/>`_.

6. The first time you log in, you will see a button labelled "Complete subscription" - this will create the link between your Aiven account and your AWS account.  After pressing this button, you will be able to choose your Aiven organization name and your first Aiven project name.  If you have any existing Aiven projects which you want to be moved to your new AWS subscription, this organization name is the one which you will need for that migration.

7. You are now ready to create your first project and deploy services.

.. note:: 
   Note the URL is https://console.aws.aiven.io - this uses a different account system than https://console.aiven.io.  When coming back to Aiven in the future, you will need to use https://console.aws.aiven.io to login.

.. note:: 
   When you view the Aiven subscription in your AWS web console, you will see a link to **Set up your account**.  You can use this link to complete the subscription process if anything goes wrong during the steps listed here.

