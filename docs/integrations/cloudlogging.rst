Google Cloud Logging
====================

You can send your service logs to Google Cloud Logging to store, search, analyze, monitor, and alert on log data from your Aiven services. 

There are two steps to setting up this integration: 

1. Create the Google Cloud Logging integration.
2. Create the integration endpoint.

You can do this using either the `Aiven Console <https://console.aiven.io/>`_ or the :doc:`CLI </docs/tools/cli>`.

Prerequisites
--------------
* You have a Google Project ID and Log ID. More information about Google Cloud projects is available in the `Google Cloud documentation <https://cloud.google.com/resource-manager/docs/creating-managing-projects>`_.
* You have Google Cloud service account credentials in JSON format to authenticate with the Google Cloud Platform. See Google Cloud's documentation for `instructions on how to create and get service account credentials <https://developers.google.com/workspace/guides/create-credentials>`_.
* The service account has permission to create log entries. See the Google Cloud documentation for information on `access control with IAM <https://cloud.google.com/logging/docs/access-control>`_.

Set up Cloud Logging integration in Aiven Console
--------------------------------------------------

Step 1. Create the integration endpoint
""""""""""""""""""""""""""""""""""""""""

#. Go to **Integration Endpoints**.

#. Select **Google Cloud Logging**.

#. Click **Add new endpoint**.

#. Enter a name.

#. Enter the **GCP Project ID** and **Log ID** from Google Cloud. 

#. Enter the **Google Service Account Credentials** in JSON format. 

#. Click **Create**.

Step 2. Add the integration endpoint to your service
"""""""""""""""""""""""""""""""""""""""""""""""""""""

#. Go to the service you want to add the logs integration to.

#. Select the **Integrations** from the left sidebar.

#. Select **Google Cloud Logging**.

#. Choose the endpoint that you created.

#. Click **Enable**.


Set up Cloud Logging integration using the CLI 
-----------------------------------------------

Step 1. Create the integration endpoint
""""""""""""""""""""""""""""""""""""""""

.. code:: 

    avn service integration-endpoint-create --project your-project-name         \
        -d "Google Cloud Logging" -t external_google_cloud_logging              \
        -c project_id=your-gcp-project-id                                       \
        -c log_id=my-aiven-service-logs                                         \
        -c service_account_credentials='{"type": "service_account"...}

Step 2. Add the integration endpoint to your service
"""""""""""""""""""""""""""""""""""""""""""""""""""""

1. Get the endpoint identifier:

   .. code-block:: shell

      avn service integration-endpoint-list --project your-project-name

2. Use the ``endpoint_id`` to attach the service to the endpoint:

   .. code-block:: shell

      avn service integration-create --project your-project-name  \
      -t external_google_cloud_logging -s your-service            \
      -D <ENDPOINT_ID>
