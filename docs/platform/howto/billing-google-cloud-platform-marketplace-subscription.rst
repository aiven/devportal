Set up Google Cloud Marketplace for Aiven services
==================================================

Aiven makes its services available through the Google Cloud Marketplace on Google Cloud Platform (GCP). This article shows the steps needed to create a subscription that links the accounts.

First, there are some steps that need to be completed on the Google Cloud Marketplace page before heading over to the Aiven console and finishing the process.

Google Cloud Marketplace setup
------------------------------

1. Navigate to `Aiven Managed Database Services on the Google Cloud Marketplace <https://console.cloud.google.com/marketplace/product/aiven-public/aiven>`_.  This page contains information about all of Aiven's services and how the marketplace subscription works.  Click the **Subscribe** button on this page.

2. Select your desired billing account, then read and agree to the terms and conditions.

3. When you are ready, click the **Subscribe** button at the bottom of the page.  You will NOT be charged by clicking this button; this only sets up a billing subscription between GCP and Aiven.  You will only be charged after deploying Aiven services.

4. You should now see a message that says  "Your order request has been sent to Aiven".  Click on the **Go to product page** button.

5. Everything is now complete in your GCP account, but you still need to setup the Aiven account.  Click on the **Manage on provider** button to go to the Aiven console to complete the process.

.. image:: /images/platform/howto/gcp-manage-on-provider.png
   :alt: Google Cloud Marketplace page after subscribing, showing the "Manage on provider" button
   :height: 249px

Aiven account setup
-------------------

6. You should now be on a signup page at Aiven, asking you for your email address to create a new account.

7. After entering your email address, you will be sent an email to confirm your registration.  Click on the link.

8. You can now proceed to the `Aiven console for GCP <https://console.gcp.aiven.io/>`_, where you can manage your Aiven services as normal.

.. image:: /images/platform/howto/gcp-console.png
   :alt: The GCP version of the Aiven web console
.. note:: 
   Note the URL is https://console.gcp.aiven.io - this uses a different account system than https://console.aiven.io.  If you have an existing Aiven account you will need to create a new Aiven GCP account using the Aiven GCP console, and when coming back to Aiven in the future you will need to use https://console.gcp.aiven.io to login.

.. note:: 
   When you view the Aiven page on GCP Marketplace, you will see a new button labeled **MANAGE ON PROVIDER**. Clicking this button will take you to the Aiven GCP Console at https://console.gcp.aiven.io.

Billing
-------

Services you deploy through your subscription are billed per hour and metering is sent from Aiven to Google. You can view this in the **Billing** section in Google Cloud.

The subscription is shown as **Use of Aiven** and the following labels show your usage per service:

- ``container_name``: This is the name of the Aiven project
- ``resource_name``: This is the name of Aiven service

.. image:: /images/platform/howto/gcp-billing.png
   :alt: Sample view of Google cloud billing page
