Move from Aiven direct billing to Google Cloud Platform Marketplace
===================================================================

Aiven makes its services available through the Google Cloud Platform Marketplace.  If you already have some services running in a project which is billied directly through Aiven, but you would like to move to a Google Cloud Platform Marketplace subscription without disrupting your services, this article shows the steps needed to gather the relevant information and submit the request.

Create a new account using a Google Cloud Platform Marketplace subscription
---------------------------------------------------------------------------

Follow the steps to :doc:`set up Google Cloud Platform Marketplace for Aiven Services <billing-google-cloud-platform-marketplace-subscription>`.  This will create a new empty project, which is where your services will be moved to.

Gather the required information
-------------------------------

Aiven will need the name of the project which currently contains your services, and the account name for the new project (in the format `E-1234-1234-1234-1234`) which is shown in the "Settings" screen for your new project in the Aiven GCP console (`https://console.gcp.aiven.io <https://console.gcp.aiven.io>`_)

Send the request to Aiven
-------------------------

Once you have the account ID, send this and the name of the project which contains the relevant services to sales@aiven.io and someone will be in touch to complete the process.

