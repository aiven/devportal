Set up Google Cloud Platform Marketplace for Aiven Services
===========================================================

Aiven makes its services available through the Google Cloud Platform Marketplace. This article shows the steps needed to create a subscription that links the accounts.

Navigate to Aiven marketplace page on GCP
-----------------------------------------

Navigate to `Aiven on the GCP marketplace <https://console.cloud.google.com/marketplace/product/aiven-public/aiven>`_. This page contains information about all of Aiven's services and how the marketplace subscription works.

Select your desired billing account, then read and agree to the the
terms and conditions.

When you are ready, click the **Subscribe** button at the bottom of the
page. You will NOT be charged by clicking this button. This only sets up
a billing subscription between GCP and Aiven. You will only be charged
after deploying Aiven services.

Finalize your Aiven GCP subscription
------------------------------------

After subscribing, check your email for a confirmation link to to create your
new account. Click the link to confirm this.

When you view the Aiven page on GCP Marketplace, you will see a new button labeled **MANAGE ON PROVIDER**. Clicking this button will take you to the Aiven GCP Console at https://console.gcp.aiven.io.

.. note:: 

    Note the URL is https://console.gcp.aiven.io This uses a different account system than https://console.aiven.io. If you have an existing Aiven account, you will need to create a new Aiven GCP account using the Aiven GCP console.

Billing
-------

Services you deploy through your subscription are billed per hour and metering is sent from Aiven to Google. You can view this in the **Billing** section in Google Cloud.

The subscription is shown as **Use of Aiven** and the following labels show your usage per service:

- ``container_name``: This is the name of the Aiven project
- ``resource_name``: This is the name of Aiven service

.. image:: /images/platform/howto/gcp-billing.png
   :alt: Sample view of Google cloud billing page
