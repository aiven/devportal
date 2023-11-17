Integrate Google BigQuery endpoints with Aiven services
========================================================

Google BigQuery is a serverless, highly scalable data warehouse that can be used to store and analyze large amounts of data. By integrating Google BigQuery endpoints with Aiven services, you can easily combine powerful data analysis from BigQuery with the convenience of Aiven's managed cloud platform. You can achieve this using the `Aiven Console <https://console.aiven.io/>`_ or by using the :doc:`Aiven CLI </docs/tools/cli>` commands.

Prerequisites
--------------

* **Google Project ID**: You have a Google Project ID. For more information, see `Google Cloud documentation <https://cloud.google.com/resource-manager/docs/creating-managing-projects>`_.
* **Google Cloud Service Account Credentials**: You have Google Cloud service account credentials in JSON format to authenticate with the Google Cloud Platform. For instructions on how to create and get service account credentials, see `Google Cloud's documentation <https://developers.google.com/workspace/guides/create-credentials>`_.
* **Service account permissions**: Your service account is granted the necessary permissions to create log entries. For information on access control with IAM, see `Google Cloud's access control documentation <https://cloud.google.com/logging/docs/access-control>`_.


Integration using Aiven Console
--------------------------------------

Step 1: Create integration endpoints
`````````````````````````````````````
1. In the `Aiven Console <https://console.aiven.io/>`_, choose your project. 
2. Select **Integration endpoints**  on the left sidebar. 
3. Choose Google BigQuery, and click **Add new point** or **Create new**. 
4. Enter the following details: 
   
   * **Endpoint name**: Enter a name for the integration endpoint. For example, ``BigQuery_Aiven_Integration``.
   * **GCP Project ID**: The identifier associated with your Google Cloud Project where BigQuery is set up. For example, ``my-gcp-project-12345``.
   * **Google Service Account Credentials**: The JSON formatted credentials obtained from your Google Cloud Console for service account authentication. For example: 

   ::
    
        {
            "type": "service_account",
            "project_id": "my-gcp-project-12345",
            "private_key_id": "abcd1234",
            ...
        }

5. Click **Create**. 

Step 2: Link the integration endpoint to your service
````````````````````````````````````````````````````````
1. In the `Aiven Console <https://console.aiven.io/>`_, access the service where you plan to integrate Google BigQuery.
2. Choose **Integrations** from the left sidebar.
3. Select **Google BigQuery**.
4. Choose the endpoint that you created.
5. Click **Enable**.

Integration using Aiven CLI
------------------------------------------

Step 1. Create integration endpoints
``````````````````````````````````````
To create a new integration endpoint that can be used to connect to a BigQuery service, use the :ref:`avn service integration-endpoint-create <avn_service_integration_endpoint_create>` command with the required parameters.

.. code::

    avn service integration-endpoint-create \
    --project <project_name> \
    --endpoint-name <endpoint_name> \
    --endpoint-type external_bigquery \
    --user-config-json '{
        "project_id": "<gcp_project_id>",
        "service_account_credentials": {
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "client_email": "<service_account_email>",
            "client_id": "<client_id>",
            "client_x509_cert_url": "<client_x509_cert_url>",
            "private_key": "<private_key_content>",
            "private_key_id": "<private_key_id>",
            "project_id": "<service_account_project_id>",
            "token_uri": "https://oauth2.googleapis.com/token",
            "type": "service_account"
        }
    }'


where:

* ``--project``: Name of the Google project where you want to create the integration endpoint.
* ``--endpoint-name``: Name of the integration endpoint you are creating. Replace ``your_endpoint_name`` with your desired endpoint name.
* ``--endpoint-type``: The type of integration endpoint. For example, if it's an external BigQuery service, enter ``external_bigquery``.
* ``--user-config-json``: A JSON object with custom configurations for the integration endpoint. The JSON object should include the following fields:

  *  ``project_id``: Your actual Google Cloud Platform project ID.
  *  ``service_account_credentials``: An object that holds the necessary credentials for authenticating and accessing the external Google BigQuery service. This object should include the following fields:

     * ``auth_provider_x509_cert_url``: The URL where the authentication provider's x509 certificate can be fetched.
     * ``auth_ur``: The URI used for authenticating requests.
     * ``client_email``: The email address associated with the service account.
     * ``client_id``: The client ID associated with the service account.
     * ``client_x509_cert_url``: The URL to fetch the public x509 certificate for the service account.
     * ``private_key``: The private key content associated with the service account.
     * ``private_key_id``: The ID of the private key associated with the service account.
     * ``project_id``: The project ID associated with the service account.
     * ``token_uri``: The URI used to obtain an access token.
     * ``type``: The type of service account, which is typically set to ``service_account``.


Step 2: Add your service to the integration endpoint
``````````````````````````````````````````````````````
1. Retrieve the endpoint identifier using the following command: 

   ::
    
    avn service integration-endpoint-list --project your-project-name

2. Using this ``endpoint_id``,  connect your Aiven service to the endpoint with the following command:
   
   ::

    avn service integration-create --project your-project-name \
    -t external_google_bigquery -s your-service-name \
    -D <ENDPOINT_ID>


